def shoe_schema(shoe) -> dict:
    return {"id": str(shoe["_id"]),
            "name": shoe["name"],
            "size": shoe["size"],
            "availability": shoe["availability"],
            "price": shoe["price"],
            "reviews": shoe["reviews"],
            "images": shoe["images"]
            }

def shoes_schema(shoes) -> list:
    return [shoe_schema(shoe) for shoe in shoes]