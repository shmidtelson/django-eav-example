<template>
  <div>
    <router-link :to="{ name: 'home'}"><button>Главная</button></router-link>
    <product-form id="edit-form" :data-id="$route.params.id"></product-form>
  </div>
</template>
<script>
import ProductForm from './admin/ProductForm'

export default {
  components: {
    ProductForm
  }
}
</script>
