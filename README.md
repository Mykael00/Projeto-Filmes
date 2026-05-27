BM Movies
 
Plataforma de Classificação e Recomendação de Filmes

---

Descrição do Projeto

O BM Movies é uma plataforma web desenvolvida para recomendação, classificação e organização de filmes, funcionando como um diário cinematográfico digital.

O sistema permitirá que usuários descubram novos filmes, salvem favoritos, organizem filmes assistidos e realizem avaliações.

---

Integrantes

- Mykael Pereira Elias
- Brena Gonçalves de Figueiredo

---

Tecnologias Utilizadas

Front-end
- Vue.js
- Vite
- Vue Router
- Axios

Back-end
- Node.js
- Express.js

Banco de Dados
- Supabase (PostgreSQL)

Versionamento
- Git e GitHub

---

Funcionalidades

- Login e autenticação
- Catálogo de filmes
- Sistema de favoritos
- Avaliação de filmes
- Diário cinematográfico digital
- Recomendações de filmes
- Interface responsiva

---

Estrutura Inicial do Projeto

bash
frontend/
backend/
docs/

---

API

Usuários
POST /register
POST /login
GET /profile

Filmes
GET /movies/popular
POST /movies
PUT /movies/:id
DELETE /movies/:id

Favoritos
POST /favorites
GET /favorites/:userId
DELETE /favorites/:id

---

Modelagem Inicial do Banco
Usuários
id
nome
email
senha
Filmes
id
titulo
descricao
categoria
imagem
Favoritos
id
usuario_id
filme_id
