import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

db=None
# uri = os.getenv('MONGODB_URI')
# Create a new client and connect to the server
uri = "mongodb+srv://ezhildhiraviya:TbdZoOXC4WovYQgO@exp-cluster.fmzwmi5.mongodb.net/?appName=exp-cluster"
client = MongoClient(uri, server_api=ServerApi('1'))

db=client['expenses-db']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)