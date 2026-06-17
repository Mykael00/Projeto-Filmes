<template>
  <section class="home">

    <div class="hero-banner">
      <div class="hero-content">
        <span class="hero-tag">🎬 BM Movies</span>

        <h1>Seu diário cinematográfico digital</h1>

        <p>
          Descubra novos filmes, organize seus favoritos
          e monte sua coleção pessoal de cinema.
        </p>
      </div>
    </div>

    <div v-if="usuarioSalvo" class="usuario-box">
      <p>
        Bem-vindo de volta,
        <strong>{{ usuarioSalvo }}</strong>
      </p>

      <button @click="irParaFilmes">
        🎬 Explorar Filmes
      </button>

    </div>

    <div v-else class="login-box">
      <h2>Entrar no BM Movies</h2>

      <label>Digite seu usuário:</label>

      <input
        v-model="usuario"
        type="text"
        placeholder="Ex: mykael2026"
        @keyup.enter="entrar"
      />

      <button @click="entrar">
        Entrar
      </button>
    </div>

    <div class="destaques">

  <h2>🔥 Filmes em Destaque</h2>

  <div
    v-if="destaques.length"
    class="cards-destaque"
  >

    <div
      v-for="filme in destaques"
      :key="filme.id"
      class="card-mini destaque-card"
    >

      <img
        :src="`https://image.tmdb.org/t/p/w500${filme.poster_path}`"
        :alt="filme.title"
      />

      <h3>
        {{ filme.title }}
      </h3>

      <p>
        {{ filme.release_date?.substring(0,4) }}
      </p>

    </div>

  </div>

</div>

    <div class="ranking">

  <h2>🏆 Top Filmes da Comunidade</h2>

  <div
    v-if="ranking.length"
    class="ranking-cards"
  >

    <div
      v-for="(filme, index) in ranking.slice(0, 3)"
      :key="filme.id"
      class="ranking-card"
    >

      <div class="medalha">

        {{
          index === 0
            ? '🥇'
            : index === 1
            ? '🥈'
            : '🥉'
        }}

      </div>

      <h3>
        {{ filme.titulo }}
      </h3>

      <p>
        ❤️ {{ filme.favoritos }}
        favorito{{ filme.favoritos > 1 ? 's' : '' }}
      </p>

    </div>

  </div>

  <p v-else>
    Nenhum filme foi favoritado ainda.
  </p>

</div>

    <p v-if="erro">{{ erro }}</p>

  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const usuario = ref('')
const usuarioSalvo = ref('')
const erro = ref('')
const ranking = ref([])
const destaques = ref([])
const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const API_BACKEND = 'http://127.0.0.1:8000'

onMounted(() => {
  usuarioSalvo.value = localStorage.getItem('usuario') || ''

  carregarRanking()
  carregarDestaques()
})

async function carregarDestaques() {
  try {
    const response = await axios.get(
      'https://api.themoviedb.org/3/trending/movie/week',
      {
        params: {
          api_key: TMDB_API_KEY,
          language: 'pt-BR'
        }
      }
    )

    destaques.value = response.data.results.slice(0, 4)

  } catch (error) {
    console.error('Erro ao carregar destaques', error)
  }
}

async function carregarRanking() {
  try {
    const response = await axios.get(
      `${API_BACKEND}/ranking`
    )

    ranking.value = response.data

  } catch (error) {
    console.error('Erro ao carregar ranking', error)
  }
}

function entrar() {
  erro.value = ''

  if (!usuario.value.trim()) {
    erro.value = 'Digite um nome de usuário.'
    return
  }

  localStorage.setItem('usuario', usuario.value.trim())
  usuarioSalvo.value = usuario.value.trim()
  usuario.value = ''
}


function irParaFilmes() {
  router.push('/filmes')
}
</script>