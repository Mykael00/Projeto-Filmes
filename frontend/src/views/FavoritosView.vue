<template>
  <section>
    <h2>Favoritos</h2>

    <p v-if="loading">Carregando favoritos...</p>

    <p v-else-if="erro">{{ erro }}</p>

    <div v-else>
      <p v-if="favoritos.length === 0">Nenhum favorito cadastrado.</p>

      <ul v-else>
        <li v-for="favorito in favoritos" :key="favorito.id">
          Usuário: <strong>{{ favorito.usuario }}</strong> —
          Filme ID: {{ favorito.filme_id }}

          <button @click="excluirFavorito(favorito.id)">
            Excluir
          </button>
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

async function carregarFavoritos() {
  try {
    loading.value = true
    const response = await axios.get('http://127.0.0.1:8000/favorites')
    favoritos.value = response.data
  } catch (error) {
    erro.value = 'Erro ao carregar favoritos.'
  } finally {
    loading.value = false
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