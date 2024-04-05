from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect():
    uri = "<ur mongo client link>"
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client['test']
        collection = db['SGBUSers']
        return collection
    except Exception as e:
        print(e)
