import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewGame from '../views/NewGame.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home Page',
    component: HomePage
  },
  {
    path: '/newgame',
    name: 'New Game',
    component: NewGame
  }
]

const router = new VueRouter({
  routes
})

export default router
