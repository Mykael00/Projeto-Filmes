<template>
  <section>
    <h2>Favoritos</h2>

    <p v-if="loading">Carregando favoritos...</p>
    <p v-else-if="erro">{{ erro }}</p>

    <div v-else>
      <p v-if="favoritos.length === 0">Nenhum favorito cadastrado.</p>

      <ul v-else>
        <li v-for="favorito in favoritos" :key="favorito.id">
          <div v-if="editandoId === favorito.id">
            <input v-model="usuarioEditado" type="text" placeholder="Usuário" />
            <input v-model="filmeIdEditado" type="number" placeholder="Filme ID" />

            <button @click="salvarEdicao(favorito.id)">Salvar</button>
            <button @click="cancelarEdicao">Cancelar</button>
          </div>

          <div v-else>
            Usuário: <strong>{{ favorito.usuario }}</strong> <br />
            Filme: <strong>{{ favorito.filme_titulo }}</strong> <br />
            Categoria: {{ favorito.filme_categoria }}

            <br />

            <button @click="iniciarEdicao(favorito)">
              Editar
            </button>

            <button @click="excluirFavorito(favorito.id)">
              Excluir
            </button>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const favoritos = ref([])
const loading = ref(true)
const erro = ref('')

const editandoId = ref(null)
const usuarioEditado = ref('')
const filmeIdEditado = ref('')

async function carregarFavoritos() {
  try {
    loading.value = true
    erro.value = ''

    const response = await axios.get('http://127.0.0.1:8000/favorites')
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