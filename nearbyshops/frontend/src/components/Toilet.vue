<template>

<v-layout row>
            <v-flex>
                  <v-card-text>
                    <v-layout row>
                      <v-flex> How many Toilets?</v-flex>
                      <v-flex class="pr-3">
                        <v-slider
                          v-model="slider"
                          :max="max"
                          :min="min"
                        ></v-slider>
                      </v-flex>

                      <v-flex shrink style="width: 60px">
                        <v-text-field
                          v-model="slider"
                          class="mt-0"
                          hide-details
                          single-line
                          type="number"
                        ></v-text-field>
                      </v-flex>
            </v-layout>
            </v-card-text>
                  <v-card-title primary-title>
                    <div>
                      <h3 class="headline mb-0">Nearest Toilet</h3>
                      <div>Find the nearest Toilet from a given location</div>
                      <v-text-field label="Lat/Long" v-model="latlong"></v-text-field>
                    </div>
                  </v-card-title>
                    
                  
                  <v-card-actions>
                    <v-btn flat color="orange" @click='findHospital'>Find</v-btn>
                    <v-btn flat color="orange">Share</v-btn>
                  </v-card-actions>

              </v-flex>
              <v-spacer></v-spacer>
              <v-flex>
                
                  <v-card-text>
                      <v-list two-line>
                            
                              <v-list-tile v-for="toilet in toilets.slice(0,slider)" :key="toilet.id">
                              <v-list-tile-content>
                              <div>
                                <v-list-tile-avatar>
                                  <v-icon>home</v-icon>
                                <!-- <img src=""> -->
                              </v-list-tile-avatar >
                                <v-list-tile-title class="white--text text-xs-center">  {{toilet.name}} </v-list-tile-title>
                                <v-list-tile-sub-title> {{toilet.address}} </v-list-tile-sub-title>
                             </div>
                              </v-list-tile-content>
                            </v-list-tile>
                        
                    </v-list>  
                  </v-card-text>
              </v-flex>
        
        </v-layout>


</template>

<script>
import axios from 'axios'

export default{
    data(){
        return{
        min: 0,
        max: 20,
        slider: 3,
        range: [0, 20],
        toilets:[]

        }
    },
    computed:{
      latlong(){
        return this.$store.getters.latlong
      }
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


<style>


</style>