# API with FastApi

## Description:

In this case im try FastApi Framework to practice, with a API make it to administrate shoes with CRUD

## All endpoint:

#### 1- Create

Endpoint: 
```
POST
https://api-url.test/shoes
```
Body(aplication/json):
```json
{
    "sku": "E0Q1L7XW",
    "name": "NMD_R1 PRIMEBLUE SHOES",
    "description": "Description",
    "size": ["5","5.5","6","6.5","7"],
    "availability": true,
    "price": 160,
    "reviews": "Nice too",
    "images": []
}
```
Response:
```json
{
    "http status": 201
}
```

#### 2- Read/List
Endpoint: 
```
GET
https://api-url.test/shoes
```
Response:
```json
[
    {
        "id": "_id",
        "sku": "E0Q1L7XW",
        "name": "NMD_R1 PRIMEBLUE SHOES",
        "size": ["5","5.5","6","6.5","7"],
        "availability": true,
        "price": 160,
        "reviews": ["Nice too"],
        "images": []
    }
]
```


#### 3- Update
Endpoint: 
```
PUT
https://api-url.test/shoes
```
Body(aplication/json):
```json
{
    "id": "642a3b13ac850b27cecdf81e",
    "sku": "E0Q1L7XW",
    "name": "NMD_R1 PRIMEBLUE SHOES",
    "description": "Pack your bag, lace up and get going. City adventures beckon in these NMD_R1 shoes.",
    "size": ["5","5.5","6","6.5","7"],
    "availability": true,
    "price": 260,
    "reviews": "Nice too",
    "images": []
}
```
Response:
```json
{
    "http status": 202
}
```

#### 4- Delete
Endpoint: 
```
DELETE
https://api-url.test/shoes/${id}
```

Response:
```json
{
    "http status": 204
}
```

