import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import movie_routes
from app.database import client

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client.admin.command("ping")
        print("База данных подключена")
    except Exception as e:
        print("Ошибка подключения к БД:", e)
        raise
    yield

app = FastAPI(title="Movie Collection API", lifespan=lifespan)
app.router.redirect_slashes = False

app.include_router(movie_routes.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    print(f"Приложение запущено на порту {port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)