<template>
  <div id="content-main">
    <ul class="messagelist" v-if="isAddedMessage">
      <li class="success">The product type “{{ product.title }}” was added successfully.</li>
    </ul>

    <ul class="messagelist" v-if="isUpdatedMessage">
      <li class="success">The product type “{{ product.title }}” was updated successfully.</li>
    </ul>

    <form method="post" id="producttype_form" novalidate="">
      <div>
        <fieldset class="module aligned ">
          <div class="form-row field-name">
            <div>
              <label class="required" for="id_name">Title:</label>
              <input v-model="product.title" id="id_name" type="text" class="vTextField" maxlength="250">
            </div>
          </div>

          <div class="form-row field-slug">
            <div>
              <label class="required" for="id_slug">Slug:</label>
              <input v-model="product.slug" id="id_slug" type="text" class="vTextField" maxlength="255">
            </div>
          </div>
          <div class="form-row field-slug">
            <div>
              <label class="required" for="id_product_type">Product type:</label>
              <select v-model="product.product_type" id="id_product_type">
                <option value="">---------</option>
                <option
                  :key="product_type.id"
                  v-for="product_type in productTypes"
                  v-bind:value="product_type.id"
                >
                  {{ product_type.name }}
                </option>
              </select>
            </div>
          </div>
        </fieldset>
        <div v-if="productAttributeValues.length || productNotAssignedAttributes.length" id="attrs">
          <h2>Привязанные атрибуты</h2>
          <fieldset>
            <div
              :key="productAttributeValue.id"
              v-for="productAttributeValue in productAttributeValues"
              class="row"
            >
              <div class="col-3">
                <label class="required"
                       :for="'id_product_attribute' + productAttributeValue.id">{{
                    productAttributeValue.attribute_value.attribute.name
                  }}:</label>
              </div>
              <div class="col-9">
                <multiselect
                  v-model="productAttributeValue.attribute_value"
                  label="value"
                  :multiple="false"
                  :taggable="true"
                  :id="'id_product_attribute' + productAttributeValue.id"
                  :options="productAttributeValue.variants"
                  :hide-selected="true"
                  @tag="addNewAttribute($event, productAttributeValue)"
                  @open="loadExistAttributes(productAttributeValue.attribute_value.attribute.id)"
                />
              </div>
            </div>
          </fieldset>
          <div v-if="productNotAssignedAttributes.length">
            <h2>Непривязанные атрибуты</h2>
            <fieldset>
              <div
                :key="attribute.id"
                v-for="attribute in productNotAssignedAttributes"
                class="row"
              >
                <div class="col-3">
                  <label class="required"
                         :for="'id_product_attribute' + attribute.id">{{
                      attribute.name
                    }}:</label>
                </div>
                <div class="col-6">
                  <multiselect
                    v-model="attribute.value"
                    label="value"
                    :multiple="false"
                    :taggable="true"
                    :options="attribute.variants"
                    :hide-selected="true"
                    @tag="addNewAttribute($event, attribute, exist = false)"
                  />
                </div>
                <div class="col-3">
                  <button v-on:click="addAttributeToProduct(attribute, $event)">Добавить</button>
                </div>
              </div>
            </fieldset>

          </div>

        </div>
        <div class="submit-row">
          <input type="submit" value="Save" class="default" v-on:click="onSave($event)">
        </div>
      </div>
    </form>
  </div>
</template>
<script>
import axios from 'axios';
import {getCookie} from "../../services/helper";
import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.min.css';
import {API_URL} from "../../api"

export default {
  name: "edit-product-form",
  components: {Multiselect},
  data() {
    return {
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': getCookie('csrftoken')
      },

      id: null,
      product: {
        title: '',
        slug: '',
        product_type: null,
      },
      productTypes: [], // id, name, slug
      productAttributeValues: [],
      productNotAssignedAttributes: [],
      isAddedMessage: false,
      isUpdatedMessage: false,
    };
  },
  methods: {
    showAddedMessage() {
      this.isAddedMessage = true;

      setTimeout(() => {
        this.isAddedMessage = false;
        window.location.replace(`/admin/app/product/${this.product.id}/change/`);
      }, 3000);
    },
    showUpdatedMessage() {
      this.isUpdatedMessage = true;

      setTimeout(() => {
        this.isUpdatedMessage = false;
      }, 5000);
    },
    onSave(e) {
      e.preventDefault();

      if (this.id) {
        axios.put(`${API_URL}product/${this.id}/`,
          this.product,
          {
            headers: this.headers
          })
          .then(({data}) => {
            this.product = data;
            this.onSaveCurrentAttributes()
            this.showUpdatedMessage()
          });
      } else {
        axios.post(`${API_URL}product/`,
          this.product,
          {
            headers: this.headers
          })
          .then(({data}) => {
            this.product = data;
            this.onSaveCurrentAttributes()
            this.showAddedMessage()
          });
      }
    },
    onSaveCurrentAttributes() {
      this.productAttributeValues.map(item => {
        this.saveAttribute(item);
      })
    },
    saveAttribute(attr) {
      if (attr.attribute_value) {
        attr.attribute_value_id = attr.attribute_value.id;
        axios.put(`${API_URL}product_attribute/${attr.id}/`,
          attr,
          {
            headers: this.headers
          })
          .then(() => {

          });
      }
    },
    getCurrentProduct() {
      if (!this.id) return;

      axios.get(`${API_URL}product/${this.id}/`, {
        headers: this.headers
      })
        .then(({data}) => {
          this.product = data

          this.loadNotExistAttributes();
        });
    },

    getListProductTypes() {
      axios.get(`${API_URL}product_type/`, {
        headers: this.headers
      })
        .then(({data}) => {
          this.productTypes = data
        });
    },

    getAssignedProductAttributeValues() {
      if (!this.id) return;

      axios.get(`${API_URL}product_attribute/?product_id=${this.id}`, {
        headers: this.headers
      })
        .then(({data}) => {
          data.map((item) => {
            item.variants = []
            this.loadExistAttributes(item.attribute_value.attribute.id)
            return item;
          });
          this.productAttributeValues = data;
        });
    },

    loadExistAttributes(attribute_id) {
      axios.get(`${API_URL}attribute_value/search/`, {
          params: {
            attribute_id: attribute_id,
          }
        },
        {headers: this.headers})
        .then(({data}) => {
          const index = this.productAttributeValues.findIndex(i => i.attribute_value.attribute.id === attribute_id);
          this.productAttributeValues[index].variants = data;
        });
    },

    loadNotExistsAttributesById(attribute_id) {
      axios.get(`${API_URL}attribute_value/search/`, {
        params: {
          attribute_id: attribute_id,
        }
      }, {headers: this.headers})
        .then(({data}) => {
          this.productNotAssignedAttributes[this.productNotAssignedAttributes.findIndex(i => i.id === attribute_id)].variants =
            data;
          this.$forceUpdate();
        });
    },

    loadNotExistAttributes() {
      axios.get(`${API_URL}attribute/search_not_defined_attributes/`, {
          params: {
            product_type_id: this.product.product_type,
          }
        },
        {headers: this.headers})
        // eslint-disable-next-line no-unused-vars
        .then(({data}) => {
          this.createNotAssignedItems(data);

          this.productNotAssignedAttributes.map(item => {
            item.variants = [];
            this.loadNotExistsAttributesById(item.id)
            return item;
          })
        });
    },

    createNotAssignedItems(items) {
      this.productNotAssignedAttributes = items.filter((item) => {
        return this.productAttributeValues.find(i => item.id === i.attribute_value.attribute.id) === undefined;
      });
    },

    addAttributeToProduct(attr, event) {
      event.preventDefault();

      axios.post(`${API_URL}product_attribute/`,
        {
          product: this.product.id,
          attribute_value_id: attr.value.id
        },
        {
          headers: this.headers
        })
        .then(({data}) => {
          data.variants = [];
          this.productAttributeValues.push(data);
          this.loadExistAttributes(data.attribute_value.attribute.id);
          this.productNotAssignedAttributes.splice(this.productNotAssignedAttributes.findIndex(i => i.id === attr.id), 1);
          this.showUpdatedMessage();
        });
    },
    addNewAttribute(tagValue, attribute, exist = true) {
      axios.post(`${API_URL}attribute_value/`,
        {
          attribute_id: exist ? attribute.attribute_value.attribute.id : attribute.id,
          value: tagValue
        },
        {
          headers: this.headers
        })
        .then(({data}) => {
          if (exist) {
            this.loadExistAttributes(data.attribute.id);
            const index = this.productAttributeValues.findIndex(i => i.attribute_value.attribute.id === attribute.attribute_value.attribute.id);
            this.productAttributeValues[index].attribute_value = data
          }

          if (!exist) {
            this.loadNotExistAttributes();
            setTimeout(() => {

              const index = this.productNotAssignedAttributes.findIndex(i => i.id === data.attribute.id)
              this.productNotAssignedAttributes[index].value = data;
              this.$forceUpdate();
            }, 500);
          }
        });
    }
  },
  created() {
    setTimeout(() => {
      const element = document.getElementById('edit-form');

      if (element && element.dataset.id !== "None") {
        this.id = element.dataset.id
      }

      this.getCurrentProduct();
      this.getListProductTypes();
      this.getAssignedProductAttributeValues();
    }, 500)
  },
};
</script>
