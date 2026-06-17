<template>
  <section>
    <h2>Meus Favoritos</h2>

<div v-if="usuario">
  <p>
    Usuário ativo:
    <strong>{{ usuario }}</strong>
  </p>
</div>

<div v-else>
  <p>Você precisa criar ou selecionar um usuário para ver seus favoritos.</p>

  <button @click="irParaHome">
    👤 Criar Usuário
  </button>
</div>

<p v-if="loading">Carregando favoritos...</p>
<p v-else-if="erro">{{ erro }}</p>

<div v-else-if="usuario">

  <p v-if="favoritos.length === 0">
    Nenhum favorito cadastrado para este usuário.
  </p>

  <div
    v-else
    class="favoritos-grid"
  >

    <div
      v-for="favorito in favoritos"
      :key="favorito.id"
      class="favorito-card"
    >

      <div v-if="editandoId === favorito.id">

        <input
          v-model="usuarioEditado"
          type="text"
          placeholder="Usuário"
        />

        <input
          v-model="filmeIdEditado"
          type="number"
          placeholder="Filme ID"
        />

        <button @click="salvarEdicao(favorito.id)">
          Salvar
        </button>

        <button @click="cancelarEdicao">
          Cancelar
        </button>

      </div>

      <div v-else>

        <img
          v-if="favorito.poster_url"
          :src="favorito.poster_url"
          :alt="favorito.filme_titulo"
          class="favorito-poster"
        />

        <h3>
          🎬 {{ favorito.filme_titulo }}
        </h3>

        <p>
          <strong>Usuário:</strong>
          {{ favorito.usuario }}
        </p>

        <p>
          ❤️ Favoritado
        </p>

        <div class="favorito-acoes">

          <button @click="iniciarEdicao(favorito)">
            Editar
          </button>

          <button @click="excluirFavorito(favorito.id)">
            Excluir
          </button>

        </div>

      </div>

    </div>

  </div>

</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const favoritos = ref([])
const loading = ref(true)
const erro = ref('')
const usuario = ref('')

const editandoId = ref(null)
const usuarioEditado = ref('')
const filmeIdEditado = ref('')

function irParaHome() {
  router.push('/')
}

async function carregarFavoritos() {
  usuario.value = localStorage.getItem('usuario') || ''

  if (!usuario.value) {
    loading.value = false
    return
  }

  try {
    loading.value = true
    erro.value = ''

    const response = await axios.get('http://127.0.0.1:8000/favorites', {
      params: {
        usuario: usuario.value
      }
    })

    favoritos.value = response.data
  } catch (error) {
    erro.value = 'Erro ao carregar favoritos.'
  } finally {
    loading.value = false
  }
}

function iniciarEdicao(favorito) {
  editandoId.value = favorito.id
  usuarioEditado.value = favorito.usuario
  filmeIdEditado.value = favorito.filme_id
}

function cancelarEdicao() {
  editandoId.value = null
  usuarioEditado.value = ''
  filmeIdEditado.value = ''
}

async function salvarEdicao(id) {
  erro.value = ''

  if (!usuarioEditado.value || !filmeIdEditado.value) {
    erro.value = 'Preencha usuário e filme ID.'
    return
  }

  try {
    await axios.put(`http://127.0.0.1:8000/favorites/${id}`, {
      usuario: usuarioEditado.value,
      filme_id: Number(filmeIdEditado.value)
    })

    cancelarEdicao()
    await carregarFavoritos()
  } catch (error) {
    erro.value = 'Erro ao editar favorito.'
  }
}

async function excluirFavorito(id) {
  const confirmar = confirm('Tem certeza que deseja excluir este favorito?')

  if (!confirmar) {
    return
  }

  try {
    await axios.delete(`http://127.0.0.1:8000/favorites/${id}`)
    await carregarFavoritos()
  } catch (error) {
    erro.value = 'Erro ao excluir favorito.'
  }
}

onMounted(() => {
  carregarFavoritos()
})
</script>