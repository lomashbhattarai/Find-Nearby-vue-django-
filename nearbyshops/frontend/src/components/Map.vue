<template>
<div id="map" class="map"></div>

</template>

<script>
export default {
    name: 'Map',
    data () {
    return {
      card_text: 'ffgsrgr',
      min: 0,
      max: 20,
      slider: 3,
      range: [0, 20],
      map: null,
      tileLayer: null,
      marker: null,
      lat: this.$store.state.lat,
      long: this.$store.state.long,
      hospitals:[]

      
    }
  },
  computed:{
   
  },
  mounted() {
    this.initMap();
    this.initLayers();
  },
  methods: {
    initMap(){
      this.map = L.map('map',{
        maxZoom: 19,
        minZoom :7
      }).setView([this.$store.state.long,this.$store.state.lat],7);
      this.tileLayer = L.tileLayer(
        'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
        {
          maxZoom: 18,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
        }
      );
      this.tileLayer.addTo(this.map);

      this.marker = L.marker(new L.LatLng(28, 85.2), {
      draggable: true
      }).addTo(this.map);

      this.marker.on('dragend',(e) => {
        this.$store.commit('getLatLong',[this.marker.getLatLng().lat,this.marker.getLatLng().lng]);
        
      })


    },
    initLayers(){
      this.$store.getters.markers.map((coord)=>{
        L.marker(new L.LatLng(coord[0],coord[1])).addTo(this.map);

      })
    }
    
}
}
</script>

<style scoped>
</style>