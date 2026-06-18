BM Movies

Plataforma de Pesquisa, Organização e Recomendação de Filmes

O BM Movies é uma aplicação web desenvolvida com o objetivo de permitir que usuários pesquisem filmes, organizem seus favoritos e descubram títulos populares através de rankings e destaques da comunidade.

O projeto foi desenvolvido como atividade acadêmica utilizando conceitos de desenvolvimento Full Stack, integrando frontend, backend, banco de dados e APIs externas.

---

Integrantes

- Brena Gonçalves de Figueiredo
- Mykael Pereira Elias

---

Tecnologias Utilizadas

Frontend

- Vue.js 3
- Vite
- Vue Router
- Axios
- CSS3

Backend

- Python
- FastAPI
- Uvicorn

Banco de Dados

- PostgreSQL
- Supabase

APIs Externas

- TMDb (The Movie Database)

Versionamento

- Git
- GitHub

Deploy

- Render

---

Objetivo do Projeto

Desenvolver uma plataforma web que permita aos usuários:

- Pesquisar filmes reais utilizando uma API externa.
- Visualizar informações detalhadas sobre os filmes.
- Criar uma lista personalizada de favoritos.
- Visualizar rankings e destaques da comunidade.
- Aplicar conceitos de desenvolvimento Full Stack estudados durante a disciplina.

---

Funcionalidades

Login de Usuário

O sistema possui uma tela de login simples que permite ao usuário acessar sua área personalizada.

Pesquisa de Filmes

Integração com a API TMDb para pesquisa de filmes em tempo real.

Informações exibidas:

- Título
- Pôster
- Ano de lançamento
- Sinopse

Favoritos

O usuário pode adicionar filmes à sua lista de favoritos.

Os favoritos ficam associados ao usuário e são armazenados no banco de dados.

Ranking da Comunidade

Exibição dos filmes mais populares cadastrados pelos usuários da plataforma.

Filmes em Destaque

Seção dedicada à exibição de filmes destacados na página inicial.

Interface Responsiva

Layout adaptado para diferentes tamanhos de tela.

---

Arquitetura do Sistema

Frontend (Vue.js)
        │
        ▼
Backend (FastAPI)
        │
        ▼
PostgreSQL (Supabase)
        │
        ▼
TMDb API

---

Estrutura do Projeto

Projeto-Filmes/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   ├── router/
│   │   ├── components/
│   │   └── assets/
│   │
│   ├── public/
│   ├── .env
│   └── package.json
│
├── docs/
│
└── README.md

---

API REST

Movies

Método| Endpoint
GET| /movies
GET| /movies/{id}
POST| /movies
PUT| /movies/{id}
DELETE| /movies/{id}

Favorites

Método| Endpoint
GET| /favorites
POST| /favorites
PUT| /favorites/{id}
DELETE| /favorites/{id}

---

Banco de Dados

Tabela Movies

Campo| Tipo
id| bigint
titulo| text
categoria| text

Tabela Favorites

Campo| Tipo
id| bigint
usuario| text
filme_id| bigint

---

Como Executar o Projeto

Backend

cd backend

pip install -r requirements.txt

uvicorn main:app --reload

API disponível em:

http://127.0.0.1:8000

Documentação automática:

http://127.0.0.1:8000/docs

Frontend

cd frontend

npm install

npm run dev

Variáveis de Ambiente

Criar um arquivo ".env" dentro da pasta frontend:

VITE_TMDB_API_KEY=SUA_CHAVE_DA_TMDB

---

Conceitos Aplicados

- Desenvolvimento Full Stack
- Arquitetura Cliente-Servidor
- Consumo de APIs REST
- Integração com APIs Externas
- Persistência de Dados
- Controle de Versão com Git
- Componentização em Vue.js
- Comunicação Frontend ↔ Backend
- Banco de Dados Relacional

---

Melhorias Futuras

- Sistema de avaliações por estrelas
- Recomendações personalizadas
- Autenticação com JWT
- Perfis de usuário
- Comentários e avaliações
- Lista de filmes assistidos
- Dashboard administrativo

---

Licença

Projeto desenvolvido para fins acadêmicos na disciplina de Desenvolvimento Web.
