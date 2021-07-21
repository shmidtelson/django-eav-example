import HomePage from './components/HomePage'
import ProductForm from "./components/admin/ProductForm";
import ProductFormFront from "./components/ProductFormFront";

export const routes = [
  {path: '', component: HomePage},
  {path: '/product/edit/:id', component: ProductForm},
  {path: '/admin/app/product/new/', component: ProductForm},
  {path: '/admin/app/product/:id/change/', component: ProductFormFront},
]
