from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# 웹 스크래핑할 때 쓰는 beautifulSoap
import requests
from bs4 import BeautifulSoup

# data를 부르기 위한 서버 (pymongo)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
		# 2. meta tag를 스크래핑하기
		# 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})


# 메모를 작성하기 위해 서버가 전달받아야하는 정보는 다음 두 가지입니다.
# - URL(url_give)
# - 코멘트(comment_give)

# 그리고 URL를 meta tag를 스크래핑해서 아래 데이터를 저장(Create)합니다.
# - URL(url)
# - 제목(title)
# - 설명(desc)
# - 이미지URL(image)
# - 코멘트(comment)

# 따라서 서버 로직은 다음 단계로 구성되어야 합니다.
# 1. 클라이언트로부터 데이터를 받기
# 2. meta tag를 스크래핑하기
# 3. mongoDB에 데이터를 넣기

@app.route('/memo', methods=['POST'])
def post_articles():
    # 1. 클라이언트로부터 데이터 받기 (입력한 url, 입력한 comment)
    url_receive = response.form['url_give']
    comment_receive = response.form['comment_give']

    # 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {'url':url_receive, 'title':url_title, 'description':url_description, 'image':url_image, 'comment':comment_receive}

    # 3. mongoDB에 데이터 넣기
    db.articles.insert_one(article)

    return jsonify({'result':'success'})
