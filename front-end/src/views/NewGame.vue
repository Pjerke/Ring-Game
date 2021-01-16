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
                v-model="stake"
                :rules="[rules.required, rules.number]"
                label="Stake per player"
                outlined
            ></v-text-field>
        </v-form>
    </v-card-text>
    <v-divider/>
    <v-card-actions>
        <v-btn 
            class="mx-auto"
            color="blue"
            x-large
            :disabled="!valid"
            @click="click">Start</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NewGame',
  data: () => ({
      items: [3,4,5,6],
      nPlayers: 4,
      players: ['', '', '', '', '', ''],
      stake: '',
      rules: {
        required: (v) => !!v || 'Required',
        number: (v) => !isNaN(Number(v)) || 'Must be a number',
      },
      valid: false
  }),
  methods: {
        click () {
            console.log(this.players)
            axios.get('http://localhost:5000/newgame')
                .then((res) => {
                    console.log(res)
                    axios.get('http://localhost:5000/test')
                        .then((res) => {
                            console.log(res)
                        })
                        .catch((error) => {
                            console.error(error)
                        })
                        // .finally(() => {
                        // })
                })
                .catch((error) => {
                    console.error(error)
                })
                // .finally(() => {
                // })
            
        }
  }
}
</script>

<style>
.v-select__selections input { display: none}
</style>
