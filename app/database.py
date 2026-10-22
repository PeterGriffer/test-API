import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/movies_db")
client = MongoClient(MONGODB_URI)
db = client["movies_db"]
#db = client.get_default_database()
movies_collection = db["movies"]