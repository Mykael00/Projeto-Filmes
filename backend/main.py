from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movie(BaseModel):
    titulo: str
    categoria: str


@app.get("/")
def home():
    return {"message": "API de filmes funcionando!"}


@app.get("/movies")
def listar_filmes():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, titulo, categoria FROM movies ORDER BY id")
            rows = cur.fetchall()

    return [
        {"id": r[0], "titulo": r[1], "categoria": r[2]}
        for r in rows
    ]


@app.get("/movies/{movie_id}")
def buscar_filme(movie_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, titulo, categoria FROM movies WHERE id = %s",
                (movie_id,)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    return {"id": row[0], "titulo": row[1], "categoria": row[2]}


@app.post("/movies")
def criar_filme(movie: Movie):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO movies (titulo, categoria)
                VALUES (%s, %s)
                RETURNING id, titulo, categoria
                """,
                (movie.titulo, movie.categoria)
            )
            row = cur.fetchone()
            conn.commit()

    return {"id": row[0], "titulo": row[1], "categoria": row[2]}


@app.put("/movies/{movie_id}")
def atualizar_filme(movie_id: int, movie: Movie):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE movies
                SET titulo = %s, categoria = %s
                WHERE id = %s
                RETURNING id, titulo, categoria
                """,
                (movie.titulo, movie.categoria, movie_id)
            )
            row = cur.fetchone()
            conn.commit()

    if row is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    return {"id": row[0], "titulo": row[1], "categoria": row[2]}


@app.delete("/movies/{movie_id}")
def deletar_filme(movie_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM movies WHERE id = %s RETURNING id",
                (movie_id,)
            )
            row = cur.fetchone()
            conn.commit()

    if row is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    return {"message": "Filme deletado com sucesso"}