from pymongo import MongoClient

db_cliente = MongoClient(
    "mongodb+srv://sam171990:jere070411@cluster0.ssfr6vw.mongodb.net/?retryWrites=true&w=majority").shoesdb

db_auth_user_cliente = MongoClient(
    "mongodb+srv://sam171990:jere070411@cluster0.ssfr6vw.mongodb.net/?retryWrites=true&w=majority").users