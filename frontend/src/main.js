import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App'
import './assets/grid.css'
import {routes} from './routes'
Vue.config.productionTip = false

Vue.use(VueRouter);

const router = new VueRouter({
  routes, // сокращённая запись для `routes: routes`,
  mode: "history",

})

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app')

