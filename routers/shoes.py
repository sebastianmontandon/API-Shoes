from fastapi import APIRouter, HTTPException, status
from db.models.shoes import Shoes
from db.client import db_cliente
from db.schemas.shoes import shoe_schema, shoes_schema
from bson import ObjectId

router = APIRouter(prefix="/shoes",
                   tags=["Shoes"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

# Get specific shoe by ID
@router.get("/{id}", response_model=Shoes)
async def user(id: str):
    return shoe_schema(db_cliente.shoes.find_one(ObjectId(id)))

# List shoes
@router.get("/", response_model=list[Shoes])
async def all_shoes():
    return shoes_schema(db_cliente.shoes.find())

# Create new shoe
@router.post("/", response_model=Shoes, status_code=status.HTTP_201_CREATED)
async def add_shoe(shoe: Shoes):

    if type(shoe_exist("sku", shoe.sku)) == Shoes:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED, detail="Shoe already exist")

    shoe_dict = dict(shoe)
    del shoe_dict["id"]

    id = db_cliente.shoes.insert_one(shoe_dict).inserted_id
    new_shoe = shoe_schema(db_cliente.shoes.find_one({"_id": id}))
    return Shoes(**new_shoe)

# Update Shoe
@router.put("/", status_code=status.HTTP_202_ACCEPTED)
async def shoe_update(shoe: Shoes):

    if type(shoe_exist("_id", ObjectId(shoe.id))) != Shoes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shoe not found")

    shoe_dic = dict(shoe)
    del shoe_dic["id"]
    try:
        db_cliente.shoes.find_one_and_replace(
            {"_id": ObjectId(shoe.id)},  shoe_dic)
    except:
        return {"error_message": "Shoe cannot updated"}

    return {"message": "Shoe correct updated"}

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shoe(id: str):
    found = db_cliente.shoes.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error_message": "Shoe cannot deleted"}


# Functions

def shoe_exist(fiel: str, key):
    try:
        shoe = shoe_schema(db_cliente.shoes.find_one({fiel: key}))
        return Shoes(**shoe)
    except:
        return {"error_message": "Something going worng"}
