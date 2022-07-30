import pymongo

import main

client = pymongo.MongoClient("mongodb+srv://RootJix:Jix@clusterjix.eh0oq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data={

    "name" : "Jitendra",
    "MailId": "JIx@gmail.com",
    "Subject":["maths", "english","science"]
}

database = client['myinfo']
collections= database["jix"]
collections.insert_one(data)