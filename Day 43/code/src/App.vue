<template>
  <Header title="Mars' weather" :days="this.days" @day-changed="dayChanged"/>
  <Weather :weather='this.weather' />
</template>

<script>
import Header from './components/Header'
import Weather from './components/Weather'

export default {
  name: 'Demo',
  components: {
    Header,
    Weather
  },
  data(){
    return {
      'days': [],
      'weather': {}
    }
  },
  methods: {
    dayChanged(day){
      this.weather = this.data[day]
    },
    async fetchWeather(){
      //const res = await fetch('http://localhost:3000/get')
      const res = await fetch('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
      const data = await res.json()
      return data
    }
  },
  async created(){
    this.data = await this.fetchWeather()
    this.days = this.data['sol_keys']
    this.weather = this.data[this.days[0]]
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
