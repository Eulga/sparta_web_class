from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.r2nnoby.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'범죄도시3'},{'$set':{'rate':0}})
