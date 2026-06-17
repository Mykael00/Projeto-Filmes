<template>
  <div class="login-page">


<div class="login-card">

  <h1>🎬 BM Movies</h1>

  <p>
    Sua plataforma para descobrir e organizar filmes.
  </p>

  <input
    v-model="usuario"
    type="text"
    placeholder="Usuário"
  />

  <input
    v-model="senha"
    type="password"
    placeholder="Senha"
    @keyup.enter="entrar"
  />

  <button @click="entrar">
    Entrar
  </button>

  <p
    v-if="erro"
    class="erro-login"
  >
    {{ erro }}
  </p>

</div>


  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const usuario = ref('')
const senha = ref('')
const erro = ref('')

function entrar() {

  erro.value = ''

  if (!usuario.value.trim()) {
    erro.value = 'Digite um usuário.'
    return
  }

  if (!senha.value.trim()) {
    erro.value = 'Digite uma senha.'
    return
  }

  localStorage.setItem('logado', 'true')
  localStorage.setItem('usuario', usuario.value)

  router.push('/')
}
</script>
