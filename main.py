from fastapi import FastAPI
from routers import shoes, jwt_authentication


app = FastAPI()

app.include_router(jwt_authentication.router)
app.include_router(shoes.router)