```vue
<template>
  <section>
    <h2>Buscar filmes</h2>

    <div v-if="usuario">
      <p>
        Usuário ativo:
        <strong>{{ usuario }}</strong>
      </p>
    </div>

    <div v-else>
      <p>
        Você precisa criar ou selecionar um usuário antes de favoritar filmes.
      </p>

      <button @click="irParaHome">
        👤 Criar Usuário
      </button>
    </div>

    <div>
      <label>Pesquisar filme:</label>

      <input
        v-model="termoBusca"
        type="text"
        placeholder="Ex: Batman, Matrix, Avatar"
        @keyup.enter="buscarFilmes"
      />

      <button @click="buscarFilmes">
        Pesquisar
      </button>
    </div>

    <p v-if="mensagem">{{ mensagem }}</p>
    <p v-if="loading">Carregando filmes...</p>
    <p v-if="erro">{{ erro }}</p>

    <div v-if="filmesTmdb.length > 0">
      <h3>Resultados da busca</h3>

      <div
        v-for="filme in filmesTmdb"
        :key="filme.id"
        class="movie-card"
      >
        <img
          v-if="filme.poster_path"
          :src="`https://image.tmdb.org/t/p/w200${filme.poster_path}`"
          :alt="filme.title"
        />

        <div>
          <h3>{{ filme.title }}</h3>

          <p>
            <strong>Ano:</strong>
            {{
              filme.release_date
                ? filme.release_date.substring(0, 4)
                : 'Não informado'
            }}
          </p>

          <p>
            <strong>Sinopse:</strong>
            {{ filme.overview || 'Sinopse não disponível.' }}
          </p>

          <button @click="favoritarFilmeTmdb(filme)">
            Favoritar
          </button>
        </div>
      </div>
    </div>

    <div v-else-if="buscaRealizada && !loading">
      <p>Nenhum filme encontrado.</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const API_BACKEND = 'http://127.0.0.1:8000'
const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY

const usuario = ref('')
const termoBusca = ref('')
const filmesTmdb = ref([])

const loading = ref(false)
const erro = ref('')
const mensagem = ref('')
const buscaRealizada = ref(false)

onMounted(() => {
  usuario.value = localStorage.getItem('usuario') || ''
})

function irParaHome() {
  router.push('/')
}

async function buscarFilmes() {
  mensagem.value = ''
  erro.value = ''
  filmesTmdb.value = []

  if (!termoBusca.value) {
    erro.value = 'Digite o nome de um filme para pesquisar.'
    return
  }

  try {
    loading.value = true
    buscaRealizada.value = true

    const response = await axios.get(
      'https://api.themoviedb.org/3/search/movie',
      {
        params: {
          api_key: TMDB_API_KEY,
          query: termoBusca.value,
          language: 'pt-BR'
        }
      }
    )

    filmesTmdb.value = response.data.results
  } catch (error) {
    erro.value = 'Erro ao buscar filmes na TMDb.'
  } finally {
    loading.value = false
  }
}

async function favoritarFilmeTmdb(filme) {
  mensagem.value = ''
  erro.value = ''

  if (!usuario.value) {
    erro.value =
      'Entre com um usuário na página inicial antes de favoritar.'
    return
  }

  try {
    const categoria =
      filme.genre_ids && filme.genre_ids.length > 0
        ? `Gênero TMDb ID: ${filme.genre_ids[0]}`
        : 'Categoria não informada'

    const filmeCriado = await axios.post(`${API_BACKEND}/movies`, {
      titulo: filme.title,
      categoria
    })

    await axios.post(`${API_BACKEND}/favorites`, {
      usuario: usuario.value,
      filme_id: filmeCriado.data.id
    })

    mensagem.value = 'Filme adicionado aos favoritos!'
  } catch (error) {
    if (
      error.response &&
      error.response.data &&
      error.response.data.detail
    ) {
      erro.value = error.response.data.detail
    } else {
      erro.value = 'Erro ao favoritar filme.'
    }
  }
}
</script>
```
