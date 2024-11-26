from pymongo import MongoClient

def connect_to_mongodb():
    # Connexion à MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Changez l'URL si nécessaire
    db = client["RI_Project"]  # Nom de la base de données
    return db
