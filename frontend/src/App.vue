<template>
  <div class="app">
    <nav class="navbar">
      <h1>BM Movies</h1>

      <div class="links">
        <RouterLink to="/">Início</RouterLink>
        <RouterLink to="/filmes">Filmes</RouterLink>
        <RouterLink to="/cadastrar">Cadastrar</RouterLink>
        <RouterLink to="/favoritos">Favoritos</RouterLink>
      </div>
    </nav>

    <RouterView />
  </div>
</template>