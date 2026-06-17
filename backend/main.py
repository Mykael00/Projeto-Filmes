from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
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
    poster_url: Optional[str] = None


class Favorite(BaseModel):
    usuario: str
    filme_id: int


@app.get("/")
def home():
    return {"message": "API de filmes funcionando!"}


@app.get("/movies")
def listar_filmes():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(""" SELECT id, titulo, categoria, poster_url FROM movies ORDER BY id """)
            rows = cur.fetchall()

    return [
    {
        "id": r[0],
        "titulo": r[1],
        "categoria": r[2],
        "poster_url": r[3]
    }
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
                INSERT INTO movies (
    titulo,
    categoria,
    poster_url
)
VALUES (%s, %s, %s)
RETURNING id, titulo, categoria, poster_url
                """,
                (
    movie.titulo,
    movie.categoria,
    movie.poster_url
)
            )
            row = cur.fetchone()
            conn.commit()

    return {
    "id": row[0],
    "titulo": row[1],
    "categoria": row[2],
    "poster_url": row[3]
}


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


@app.get("/favorites")
def listar_favoritos(usuario: Optional[str] = None):
    with get_connection() as conn:
        with conn.cursor() as cur:
            if usuario:
                cur.execute(
                    """
                    SELECT
                        f.id,
                        f.usuario,
                        f.filme_id,
                        m.titulo,
                        m.categoria,
                        m.poster_url
                    FROM favorites f
                    JOIN movies m ON f.filme_id = m.id
                    WHERE LOWER(f.usuario) = LOWER(%s)
                    ORDER BY f.id
                    """,
                    (usuario,)
                )
            else:
                cur.execute(
                    """
                   SELECT
                        f.id,
                        f.usuario,
                        f.filme_id,
                        m.titulo,
                        m.categoria,
                        m.poster_url
                    FROM favorites f
                    JOIN movies m ON f.filme_id = m.id
                    ORDER BY f.id
                    """
                )

            rows = cur.fetchall()

    return [
    {
        "id": r[0],
        "usuario": r[1],
        "filme_id": r[2],
        "filme_titulo": r[3],
        "filme_categoria": r[4],
        "poster_url": r[5]
    }
    for r in rows
]


@app.get("/favorites/{favorite_id}")
def buscar_favorito(favorite_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, usuario, filme_id FROM favorites WHERE id = %s",
                (favorite_id,)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")

    return {
        "id": row[0],
        "usuario": row[1],
        "filme_id": row[2]
    }


@app.post("/favorites")
def criar_favorito(favorite: Favorite):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id FROM favorites
                WHERE LOWER(usuario) = LOWER(%s) AND filme_id = %s
                """,
                (favorite.usuario, favorite.filme_id)
            )
            favorito_existente = cur.fetchone()

            if favorito_existente:
                raise HTTPException(
                    status_code=400,
                    detail="Este filme já está nos favoritos deste usuário"
                )

            cur.execute(
                """
                INSERT INTO favorites (usuario, filme_id)
                VALUES (%s, %s)
                RETURNING id, usuario, filme_id
                """,
                (favorite.usuario, favorite.filme_id)
            )
            row = cur.fetchone()
            conn.commit()

    return {
        "id": row[0],
        "usuario": row[1],
        "filme_id": row[2]
    }


@app.put("/favorites/{favorite_id}")
def atualizar_favorito(favorite_id: int, favorite: Favorite):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE favorites
                SET usuario = %s, filme_id = %s
                WHERE id = %s
                RETURNING id, usuario, filme_id
                """,
                (favorite.usuario, favorite.filme_id, favorite_id)
            )
            row = cur.fetchone()
            conn.commit()

    if row is None:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")

    return {
        "id": row[0],
        "usuario": row[1],
        "filme_id": row[2]
    }


@app.delete("/favorites/{favorite_id}")
def deletar_favorito(favorite_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM favorites WHERE id = %s RETURNING id",
                (favorite_id,)
            )
            row = cur.fetchone()
            conn.commit()

    if row is None:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")

    return {"message": "Favorito deletado com sucesso"}

@app.get("/ranking")
def ranking_filmes():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    m.id,
                    m.titulo,
                    COUNT(f.id) as total_favoritos
                FROM movies m
                INNER JOIN favorites f
                    ON m.id = f.filme_id
                GROUP BY m.id, m.titulo
                ORDER BY total_favoritos DESC, m.titulo ASC
                LIMIT 10
            """)

            rows = cur.fetchall()

    return [
        {
            "id": row[0],
            "titulo": row[1],
            "favoritos": row[2]
        }
        for row in rows
    ]