from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

all_users = list(db.users.find({}))

same_ages = list(db.users.find({'age':21}))

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user)

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)