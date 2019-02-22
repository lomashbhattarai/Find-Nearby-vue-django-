<template>
<div>
  <ToolBar></ToolBar>
  <v-container>
    <v-card dark class="elevation-20">
          <Map></Map>
          <router-view></router-view>
          <!-- <Hospital></Hospital> -->
    </v-card>
  </v-container>
  </div>
</template>

<script>



/* eslint-disable no-console */
import HelloWorld from './components/HelloWorld'
import Map from './components/Map'
import ToolBar from './components/ToolBar'
import Hospital from './components/Hospital'


export default {
  name: 'App',
  components: {
    HelloWorld,
    Map,
    ToolBar,
    Hospital
  },
  data () {
    return {
      card_text: 'ffgsrgr',
      min: 0,
      max: 20,
      slider: 3,
      range: [0, 20],
      hospitals:[]

      
    }
  },
  computed:{
    /* latlong: function(){
      if(this.lat && this.long){
        return `${this.lat.toPrecision(4)},${this.long.toPrecision(4)}`
      }
      else{
        return ''
      }
      
    } */
  },
  methods: {
    findHospital(){
      var vm= this;
      axios.get(process.env.API_URL+`/api/hospital/${this.lat}/${this.long}`).then(function(response){
        vm.hospitals = response.data.results
        console.log(vm.hospitals)
      })

    }

  }
}
</script>

<style scoped>
.map{
  height: 400px;
}
</style>