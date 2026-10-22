from bson import ObjectId
from bson.errors import InvalidId
from app.database import movies_collection

def get_all_movies():
    movies = []
    for doc in movies_collection.find():
        doc["_id"] = str(doc["_id"])
        movies.append(doc)
    return movies

def get_movie_by_id(uid: str):
    try:
        doc = movies_collection.find_one({"_id": ObjectId(uid)})
    except InvalidId:
        return None
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

def create_movie(movie: dict):
    result = movies_collection.insert_one(movie)
    movie["_id"] = str(result.inserted_id)
    return movie

def update_movie(uid: str, data: dict):
    try:
        movies_collection.update_one(
            {"_id": ObjectId(uid)}, {"$set": data}
        )
    except InvalidId:
        return None
    return get_movie_by_id(uid)

def delete_movie(uid: str):
    try:
        result = movies_collection.delete_one({"_id": ObjectId(uid)})
        return result.deleted_count > 0
    except InvalidId:
        return False

def delete_all_movies():
    movies_collection.delete_many({})