import Vue from 'vue'
import ProductForm from './components/admin/ProductForm'

Vue.config.productionTip = false

Vue.component(ProductForm.name, ProductForm)

new Vue({
  render: h => h(ProductForm),
}).$mount('#edit-form')

