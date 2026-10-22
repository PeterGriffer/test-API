from fastapi import APIRouter, HTTPException
from app.models.movie import Movie
from app.services import movie_service as svc

router = APIRouter(prefix="/v1/movies", tags=["movies"])

@router.get("")
def list_movies():
    return svc.get_all_movies()

@router.post("", status_code=201)
def add_movie(movie: Movie):
    return svc.create_movie(movie.dict(by_alias=True, exclude_none=True))

@router.delete("")
def remove_all_movies():
    svc.delete_all_movies()
    return {"message": "Все фильмы удалены"}

@router.get("/{uid}")
def get_movie(uid: str):
    movie = svc.get_movie_by_id(uid)
    if not movie:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return movie

@router.put("/{uid}")
def update_movie_route(uid: str, movie: Movie):
    updated = svc.update_movie(uid, movie.dict(by_alias=True, exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return updated

@router.delete("/{uid}")
def remove_movie(uid: str):
    if not svc.delete_movie(uid):
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return {"message": "Фильм удалён", "id": uid}