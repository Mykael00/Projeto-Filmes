<template>
  <div class="app">

    <template v-if="$route.path !== '/login'">

      <nav class="navbar">

        <h1 class="logo">🎬 BM Movies</h1>

        <div class="links">
          <RouterLink to="/">🏠 Início</RouterLink>
          <RouterLink to="/filmes">🎬 Filmes</RouterLink>
          <RouterLink to="/favoritos">❤️ Favoritos</RouterLink>

          <RouterLink
            to="/login"
            @click="logout"
          >
            🚪 Sair
          </RouterLink>

        </div>

      </nav>

    </template>

    <main
      :class="[
        $route.path === '/login'
          ? 'conteudo-login'
          : 'conteudo'
      ]"
    >
      <RouterView />
    </main>

    <template v-if="$route.path !== '/login'">

      <footer class="footer">

        <p>🎬 BM Movies © 2026</p>

        <p>
          Projeto acadêmico desenvolvido por
          Mykael Pereira Elias e Brena Gonçalves
        </p>

      </footer>

    </template>

  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function logout() {
  localStorage.removeItem('logado')
  localStorage.removeItem('usuario')

  router.push('/login')
}
</script>