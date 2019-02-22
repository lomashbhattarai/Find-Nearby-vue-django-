import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state:{
        lat: 85.23,
        long: 27.21,
        hospitals:[{name:"testpoint",address:"unknown land",lat:25,long:85}],
        toilets:[],
        mapOf: "H"



    },
    getters:{
        latlong: function(state){
                if(state.lat && state.long){
                return `${state.lat.toPrecision(4)},${state.long.toPrecision(4)}`
                }
                else{
                return ''
                }
                
          },
        markers: function(state){
            if(state.mapOf== "H"){
                
                return state.hospitals.map((hospital)=>{
                    return [hospital.lat,hospital.long]
                })
            }

        }
        
    },
    mutations:{
        getLatLong(state,latlong){
                
                state.lat = latlong[0];
                state.long = latlong[1];

        },
        updateHospitals(state,hospitals){
            state.hospitals= hospitals
        }
    },
    actions:{

    }
})
