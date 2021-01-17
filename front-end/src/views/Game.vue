<template>
    <v-container fill-height fluid>
        <v-row class="fill-height">
            <v-col cols=3 align-self="center">
                <v-card
                    v-for="card in playerCards"
                    :key="card.name"
                    class="my-5"
                >
                    <v-card-title class="display-1">{{card.name}}</v-card-title>
                    <v-card-text class="display-2">{{card.stack}}</v-card-text>
                    <v-card-actions>
                        <v-btn
                            class="mx-auto"
                            color="#0062A2"
                            dark
                            @click="roundWin(card.name)"
                        >
                            Won round
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-spacer/>
            <v-col cols=4 align-self="center">
                <div>
                    <carousel-3d
                        width="220"
                        height="150"
                        perspective="0"
                        inverse-scaling="1000"
                        space="400"
                        display="2"
                        :count="orderedNames.length"
                        border="0"
                        bias="right"
                        ref="mycarousel"
                    >
                        <slide v-for="(name, i) in orderedNames" :key="i" :index="i">
                            <v-row class="fill-height">
                                <v-col align="center" align-self="center">{{name}}</v-col>
                            </v-row>
                        </slide>
                    </carousel-3d>
                </div>
                <v-card>
                    <v-card-text class="display-4">{{'60'}}</v-card-text>
                    <v-card-text class="display-3">Pot: {{pot}}</v-card-text>
                </v-card>
            </v-col>
            <v-spacer/>
            <v-col cols=3>

            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
import axios from 'axios'

export default {
    name: 'Game',
    components: {
        Carousel3d,
        Slide
    },
    data: () => ({
        playerCards: [],
        // activePlayer: 'Pieter',
        orderedNames: [],
        nPlayer: 2,
        pot: undefined,
        timeLeft: 60
    }),
    methods: {
        shuffleArray (array) {
            for (var i = array.length - 1; i > 0; i--) {
                var j = Math.floor(Math.random() * (i + 1))
                var temp = array[i]
                array[i] = array[j]
                array[j] = temp
            }
            return array
        },
        roundWin (name) {
            axios.post('http://localhost:5000/endround', {name})
                .then((res) => {
                    this.playerCards = res.data.players
                    // this.activePlayer = this.playerCards[0].name
                    this.pot = res.data.pot
                    this.ante = res.data.pot
                })
                .catch((error) => {
                    console.error(error)
                })
        }
    },
    computed: {},
    mounted() {
        axios.get('http://localhost:5000/getgamestate')
            .then((res) => {
                this.playerCards = res.data.players
                const playerNames = this.playerCards.map(d => d.name)
                this.orderedNames = this.shuffleArray(playerNames)
                this.nPlayers = this.orderedNames.length
                this.$refs.mycarousel.goSlide(0)
                // console.log(this.$refs.mycarousel)
                this.pot = res.data.pot
                this.ante = res.data.pot

                // start
                axios.get('http://localhost:5000/newround')
                    .then((res) => {
                        this.playerCards = res.data.players
                        this.pot = res.data.pot
                        console.log(res)
                    })
                    .catch((error) => {
                        console.error(error)
                    })
            })
            .catch((error) => {
                console.error(error)
            })
    }
}
</script>

<style>
.carousel-3d-container {
    font-size: 80px;
    color: white;
}
.carousel-3d-slide {
    background: #0062A2;
}
/* .carousel-3d-slide.left-1 {
    display: none;
} */
</style>
