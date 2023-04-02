from fastapi import FastAPI
from routers import users, jwt_authentication, users


app = FastAPI()

app.include_router(jwt_authentication.router)
app.include_router(users.router)