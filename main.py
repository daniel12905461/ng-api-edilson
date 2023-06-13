from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.socio import socios
from fastapi.middleware.cors import CORSMiddleware
from sockets.sockets import sio_app

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(socios)

app.mount('/sio', app=sio_app)
app.mount("/public", StaticFiles(directory="public"), name="public")
