import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import FilmesView from '../views/FilmesView.vue'
import FavoritosView from '../views/FavoritosView.vue'

const routes = [
  {
    path: '/login',
    component: LoginView
  },
  {
    path: '/',
    component: HomeView,
    meta: { requiresAuth: true }
  },
  {
    path: '/filmes',
    component: FilmesView,
    meta: { requiresAuth: true }
  },
  {
    path: '/favoritos',
    component: FavoritosView,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {

  const logado = localStorage.getItem('logado')

  if (to.meta.requiresAuth && !logado) {
    next('/login')
    return
  }

  if (to.path === '/login' && logado) {
    next('/')
    return
  }

  next()

})

export default router