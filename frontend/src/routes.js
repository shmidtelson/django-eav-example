import HomePage from './components/HomePage'
import ProductForm from "./components/admin/ProductForm";
import ProductFormFront from "./components/ProductFormFront";
import Product from "./components/Product";

export const routes = [
  {path: '', component: HomePage, name: 'home'},
  {path: '/product/:id', component: Product, name: 'product'},
  {path: '/admin/app/product/new/', component: ProductForm, name: 'product-new'},
  {path: '/admin/app/product/:id/change/', component: ProductFormFront, name: 'product-edit'},
]
