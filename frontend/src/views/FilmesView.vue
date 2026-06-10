<template>
  <section>
    <h2>Filmes cadastrados</h2>

    <p v-if="loading">Carregando filmes...</p>

    <p v-else-if="erro">{{ erro }}</p>

    <div v-else>
      <p v-if="filmes.length === 0">Nenhum filme cadastrado.</p>

      <ul v-else>
        <li v-for="filme in filmes" :key="filme.id">
          <strong>{{ filme.titulo }}</strong> — {{ filme.categoria }}
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const filmes = ref([])
const loading = ref(true)
const erro = ref('')

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/movies')
    filmes.value = response.data
  } catch (error) {
    erro.value = 'Erro ao carregar os filmes.'
  } finally {
    loading.value = false
  }
})
</script>