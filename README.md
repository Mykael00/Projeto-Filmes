BM Movies

Plataforma de Classificação e Recomendação de Filmes

Descrição do Projeto

O BM Movies é uma plataforma web desenvolvida para recomendação, classificação e organização de filmes, funcionando como um diário cinematográfico digital.

O sistema permite que usuários descubram novos filmes, salvem favoritos, organizem filmes assistidos e realizem avaliações.

---

Integrantes

* Mykael Pereira Elias
* Brena Gonçalves de Figueiredo

---

Tecnologias Utilizadas

Front-end

* Vue.js 3
* Vite
* Vue Router
* Axios

Back-end

* Python
* FastAPI
* Uvicorn

Banco de Dados

* Supabase
* PostgreSQL

Versionamento

* Git
* GitHub

---

Funcionalidades

* Catálogo de filmes
* Sistema de favoritos
* Organização de filmes assistidos
* Recomendações de filmes
* Interface responsiva
* API REST própria
* Integração com banco de dados PostgreSQL



Estrutura do Projeto

text
Projeto-Filmes/
│
├── frontend/
├── backend/
├── docs/
└── README.md
```

---

API REST

Movies

| Método | Endpoint |
| ------ | -------- |
| GET    | /movies  |
| POST   | /movies  |

Favorites

| Método | Endpoint   |
| ------ | ---------- |
| GET    | /favorites |
| POST   | /favorites |

---

Modelagem Inicial do Banco

Tabela Movies

| Campo     | Tipo   |
| --------- | ------ |
| id        | bigint |
| titulo    | text   |
| categoria | text   |

### Tabela Favorites

| Campo    | Tipo   |
| -------- | ------ |
| id       | bigint |
| usuario  | text   |
| filme_id | bigint |

---

Banco de Dados

O projeto utiliza PostgreSQL hospedado no Supabase.

Tabelas implementadas:

* movies
* favorites

Conexão entre FastAPI e Supabase configurada e testada com sucesso.

---

Testes

Os testes dos endpoints foram realizados através da documentação automática do FastAPI (Swagger).

Endpoints testados:

* GET /movies
* POST /movies
* GET /favorites
* POST /favorites

As evidências dos testes encontram-se na pasta:

text
docs/testes-semana2/


---

Wireframes

Os wireframes da aplicação encontram-se na pasta:

text
docs/


---

Status do Projeto

Semana 1

* Planejamento concluído
* Wireframes concluídos
* Modelagem inicial concluída
* Projeto Vue inicializado

Semana 2

* API REST implementada
* Recursos Movies e Favorites implementados
* Banco Supabase configurado
* Integração com PostgreSQL concluída
* Testes realizados
