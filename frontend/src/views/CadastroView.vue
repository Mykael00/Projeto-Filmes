<template>
  <section>
    <h2>Cadastrar Filme</h2>

    <form @submit.prevent="cadastrarFilme">
      <div>
        <label>Título do filme:</label>
        <input v-model="titulo" type="text" placeholder="Ex: Interestelar" />
      </div>

      <div>
        <label>Categoria:</label>
        <input v-model="categoria" type="text" placeholder="Ex: Ficção Científica" />
      </div>

      <button type="submit">Cadastrar</button>
    </form>

    <p v-if="mensagem">{{ mensagem }}</p>
    <p v-if="erro">{{ erro }}</p>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const titulo = ref('')
const categoria = ref('')
const mensagem = ref('')
const erro = ref('')

const router = useRouter()

async function cadastrarFilme() {
  mensagem.value = ''
  erro.value = ''

  if (!titulo.value || !categoria.value) {
    erro.value = 'Preencha título e categoria.'
    return
  }

  try {
    await axios.post('http://127.0.0.1:8000/movies', {
      titulo: titulo.value,
      categoria: categoria.value
    })

    mensagem.value = 'Filme cadastrado com sucesso!'
    titulo.value = ''
    categoria.value = ''

    setTimeout(() => {
      router.push('/filmes')
    }, 1000)
  } catch (error) {
    erro.value = 'Erro ao cadastrar filme.'
  }
}
</script>