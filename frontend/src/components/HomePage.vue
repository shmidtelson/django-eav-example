<template>
  <div>
    <h1>Hello!</h1>
    <div :key="index" v-for="(product, index) in products">
      <p>
        <b>{{ product.title }} (id: {{product.id}}) </b>
        <router-link :to="{ name: 'product', params: { id: product.id }}">Посмотреть </router-link>
        <router-link :to="{ name: 'product-edit', params: { id: product.id }}">Редактировать </router-link>
      </p>
    </div>

    <router-link :to="{ name: 'product-new'}"><button>Добавить новый</button> </router-link>
  </div>
</template>
<script>
import axios from "axios";
import {API_URL} from "../api";

export default {
  data() {
    return {
      products: []
    }
  },
  methods: {
    getProducts() {
      axios.get(`${API_URL}product/`, {
        headers: this.headers
      })
        .then(({data}) => {
          this.products = data
        });
    }
  },
  created() {
    this.getProducts();
  }
}
</script>
