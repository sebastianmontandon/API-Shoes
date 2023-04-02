from fastapi import APIRouter, HTTPException, status
from db.models.users import User
from db.client import db_cliente
from db.schemas.users import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/user",
                   tags=["User"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})


# List users
@router.get("/", response_model=list[User])
async def all_users():
    return users_schema(db_cliente.users.find())


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def add_user(user: User):
    if (type(search_user("email", user.email)) == User):
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED, detail="User already exist")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_cliente.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_cliente.users.find_one({"_id": id}))
    return User(**new_user)


def search_user(fiel: str, key):
    try:
        user = user_schema(db_cliente.users.find_one({fiel: key}))
        return User(**user)
    except:
        return {"error_message": "User not found"}