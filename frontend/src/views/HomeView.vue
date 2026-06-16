<template>
  <section class="home">
    <h2>🎬 Bem-vindo ao BM Movies</h2>

    <p class="descricao">
      Pesquise filmes, visualize informações detalhadas e monte sua coleção pessoal de favoritos.
    </p>

    <div v-if="usuarioSalvo" class="usuario-box">
      <p>
        Usuário ativo:
        <strong>{{ usuarioSalvo }}</strong>
      </p>

      <button @click="irParaFilmes">
        🎬 Ir para Filmes
      </button>

      <button @click="sairUsuario">
        Trocar usuário
      </button>
    </div>

    <div v-else class="login-box">
      <label>Digite seu usuário:</label>

      <input
        v-model="usuario"
        type="text"
        placeholder="Ex: brena2026"
        @keyup.enter="entrar"
      />

      <button @click="entrar">
        Entrar
      </button>
    </div>

    <p v-if="erro">{{ erro }}</p>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const usuario = ref('')
const usuarioSalvo = ref('')
const erro = ref('')

onMounted(() => {
  usuarioSalvo.value = localStorage.getItem('usuario') || ''
})

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

function sairUsuario() {
  localStorage.removeItem('usuario')
  usuarioSalvo.value = ''
}

function irParaFilmes() {
  router.push('/filmes')
}
</script>