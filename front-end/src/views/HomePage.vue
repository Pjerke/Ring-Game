<template>
  <div class="d-flex justify-center align-center" style="height:100%;">
      <v-img
        class="mx-2 skewed_image_button"
        width="30vw"
        max-width="30vw"
        height="80vh"
        max-height="80vh"
        src="@/assets/Appleton.jpg"
        @click="ClickStart"
      >
        <div style="color: white;">New Game</div>
      </v-img>
    <v-img
      class="mx-2 skewed_image_button"
      width="30vw"
      max-width="30vw"
      height="80vh"
      max-height="80vh"
      src="@/assets/Filler.jpg"
    >
      <div style="color: white;">Stats</div>
    </v-img>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
    }
  },
  methods: {
    ClickStart () {
      this.$router.push({ path: 'NewGame' })
    }
  }
}
</script>

<style>
.skewed_image_button {
  font-size: 50px;
  cursor: pointer;
  opacity: 0.5;
  -webkit-transform: skew(-10deg);
  -moz-transform: skew(-10deg);
  -o-transform: skew(-10deg);
}
.skewed_image_button:hover {
  opacity: 1;
}
</style>
