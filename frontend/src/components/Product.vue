<template>
  <div>
    <div v-if="Object.keys(product).length !== 0">
      <h1>PRODUCT</h1>
      <div :key="key" v-for="(value, key) in product">
        <h2>{{ key }}: {{ value }}</h2>
      </div>
      <h1>ATTRs</h1>
      <div>
        <div :key="index" v-for="(item, index) in attrs">
          <h2>{{ item.attribute_value.attribute.name }}: {{ item.attribute_value.value }}</h2>
        </div>
      </div>
    </div>
    <div v-else>
      <h1>Ничего не найдено</h1>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import {API_URL} from "../api";

export default {
  name: "product-single",
  data() {
    return {
      product: {},
      attrs: [],
    }
  },
  methods: {
    getCurrentProduct() {
      axios.get(`${API_URL}product/${this.$route.params.id}/`, {
        headers: this.headers
      })
        .then(({data}) => {
          this.product = data
        });
    },
    getAttrs() {
      axios.get(`${API_URL}product_attribute/`, {
        params: {
          product_id: this.$route.params.id,
        },
        headers: this.headers
      })
        .then(({data}) => {
          this.attrs = data
        });
    },
  },
  created() {
    this.getCurrentProduct();
    this.getAttrs();
  }
}
</script>
