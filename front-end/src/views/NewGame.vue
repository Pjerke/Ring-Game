<template>
  <v-card class="mx-auto my-auto" style="overflow-y: scroll"
    max-height="80vh">
    <v-card-title>New Game</v-card-title>
    <v-divider/>
    <v-card-text style="width:20vw;">
        <v-form ref="form"
            v-model="valid">
            <v-select
                class="mr-15"
                v-model="nPlayers"
                :items="items"
                label="Number of players"
                outlined
            ></v-select>
            <v-text-field v-for="n in nPlayers" v-bind:key="n"
                v-model="players[n-1]"
                :rules="[rules.required]"
                :label="'Player '.concat(n)"
                outlined
            ></v-text-field>
            <v-text-field
                class="mr-15"
                v-model="stakes"
                :rules="[rules.required, rules.number]"
                label="Stake per player"
                outlined
            ></v-text-field>
            <v-text-field
                class="mr-15"
                v-model="ante"
                :rules="[rules.required, rules.number]"
                label="Ante per round"
                outlined
            ></v-text-field>
        </v-form>
    </v-card-text>
    <v-divider/>
    <v-card-actions>
        <v-btn 
            class="mx-auto"
            color="#0062A2"
            dark
            :loading="loading"
            x-large
            :disabled="!valid"
            @click="click">Start
        </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NewGame',
  data: () => ({
      items: [2,3,4,5,6],
      nPlayers: 3,
      players: ['Pieter', 'Stein', 'Kevin', '', '', ''],
      stakes: 100,
      ante: 10,
      rules: {
        required: (v) => !!v || 'Required',
        number: (v) => !isNaN(Number(v)) || 'Must be a number',
      },
      valid: false,
      loading: false
  }),
  methods: {
        click () {
            this.loading = true
            const player_names = this.players.slice(0, this.nPlayers)
            const stakes = this.stakes
            const ante = this.ante
            axios.post('http://localhost:5000/newgame', 
                {player_names, stakes, ante}
                )
                .then((res) => {
                    console.log(res)
                    this.$router.push({ path: 'Game'}) //, params: {player_names, stakes, ante} })
                })
                .catch((error) => {
                    console.error(error)
                })
                .finally(() => {
                    this.loading = false
                })
        }
  }
}
</script>

<style>
.v-select__selections input { display: none}
</style>
