<template>
  <product-form id="edit-form" :data-id="$route.params.id"></product-form>
</template>
<script>
import ProductForm from './admin/ProductForm'

export default {
  components: {
    ProductForm
  }
}
</script>
