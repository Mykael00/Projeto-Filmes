from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    titulo: str
    categoria: str

class Favorite(BaseModel):
    usuario: str
    filme_id: int

movies = [
    {
        "id": 1,
        "titulo": "Interestelar",
        "categoria": "Ficção Científica"
    },
    {
        "id": 2,
        "titulo": "Batman Begins",
        "categoria": "Ação"
    }
]

favorites = []

@app.get("/")
def home():
    return {"message": "BM Movies API funcionando!"}

@app.get("/movies")
def listar_filmes():
    return movies

@app.post("/movies")
def adicionar_filme(movie: Movie):
    novo_filme = {
        "id": len(movies) + 1,
        "titulo": movie.titulo,
        "categoria": movie.categoria
    }

    movies.append(novo_filme)

    return novo_filme

@app.get("/favorites")
def listar_favoritos():
    return favorites


@app.post("/favorites")
def adicionar_favorito(favorite: Favorite):
    novo_favorito = {
        "id": len(favorites) + 1,
        "usuario": favorite.usuario,
        "filme_id": favorite.filme_id
    }

    favorites.append(novo_favorito)

    return novo_favorito