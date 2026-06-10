import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import FilmesView from '../views/FilmesView.vue'
import CadastroView from '../views/CadastroView.vue'
import FavoritosView from '../views/FavoritosView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/filmes', component: FilmesView },
  { path: '/cadastrar', component: CadastroView },
  { path: '/favoritos', component: FavoritosView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router