

class RingGame:
    def reset(self):
        self.players = []
        self.n_players = 0
        self.n_active_players = 0
        self.ante = 0
        self.pot = 0
        self.round = 0

    def new_game(self, player_names, stakes, ante):
        self.players = [Player(name, stakes) for name in player_names]
        self.n_players = len(player_names)
        self.n_active_players = len(player_names)
        self.ante = ante

    def new_round(self):
        for player in self.players:
            if player.active == False:
                continue
            ante = player.take_ante(self.ante)
            self.pot += ante

    def end_round(self, winner_name):
        # winner first
        print(winner_name)
        for player in self.players:
            if player.name != winner_name:
                continue
            other_stakes = [p.stake for p in self.players if p.name != winner_name]
            print(other_stakes)
            winnings = player.win_round(other_stakes)
            self.pot -= winnings
            break
        winner_stake = winnings / self.n_active_players if self.pot > 0 else self.ante
        for player in self.players:
            if player.name == winner_name:
                continue
            returns = player.lose_round(winner_stake)
            self.pot -= returns

    def get_game_state(self):
        player_states = [{'name': p.name, 'stack': -1*p.stack} for p in self.players]
        ordered_player_states = sorted(player_states, key=lambda d: (d['stack'], d['name']))
        for player_state in ordered_player_states:
            player_state['stack'] *= -1
        return {
            'players': ordered_player_states,
            'pot': self.pot,
            'ante': self.ante,
            'round': self.round
        }


class Player:
    def __init__(self, name, stake):
        self.name = name
        self.stack = stake
        self.active = True
        self.stake = 0

    def take_ante(self, ante):
        if ante <= self.stack:
            self.stake = ante
            self.stack -= ante
        else:
            self.stake = self.stack
            self.stack = 0
        return self.stake
    
    def win_round(self, other_stakes):
        winnings = self.stake
        for other_stake in other_stakes:
            if other_stake < self.stake:
                self.stack += other_stake
                winnings += other_stake
            else:
                self.stack += self.stake
                winnings += self.stake
        return winnings

    def lose_round(self, winner_stake):
        if self.stake > winner_stake:
            returns = self.stake - winner_stake
            self.stack += returns
        else:
            returns = 0
        self.stake = 0
        if self.stack == 0:
            self.active = False
        return returns