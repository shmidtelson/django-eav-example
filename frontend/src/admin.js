import Vue from 'vue'
import ProductForm from './components/admin/ProductForm'
import './assets/grid.css'

Vue.config.productionTip = false

Vue.component(ProductForm.name, ProductForm)

new Vue({
  render: h => h(ProductForm),
}).$mount('#edit-form')

