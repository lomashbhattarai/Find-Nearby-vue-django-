// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import VueRouter from 'vue-router'
import Routes from './routes'
import {store} from './store/store'


Vue.use(Vuetify)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: Routes

});


import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
/* eslint-disable */
new Vue({
  el: '#app',
  store,
  components: { App },
  template: '<App/>',
  router:router
})
