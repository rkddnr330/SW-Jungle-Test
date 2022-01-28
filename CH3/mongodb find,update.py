from mongodb import MongoClient
client = MongoClient('localhost',27017)
db = client.dbjungle

#1 영화제목 '매트릭스'의 평점 가져오기
movie = db.movies.find_one({'title':'매트릭스'})
star = movie['star']

#2 '매트릭스'의 평점과 같은 평점의 영화 제목들 가져오기
movies = list(db.movies.find({'star':star}))
for i in movies:
    print(i['title'])

#3 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})