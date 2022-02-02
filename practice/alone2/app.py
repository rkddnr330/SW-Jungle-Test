from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo',methods=['POST'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


@app.route('/memo',methods=['POST'])
def post_articles():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # 2. meta tag를 스크래핑하기
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')  

    og_image = soup.select_one('meta[property="og_image"]')
    og_title = soup.select_one('meta[propery="og_title"]')
    og_description = soup.select_one('meta[propery="og_description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    article = {'url':url_receive, 'title':url_title,'image':url_image, 'desc':url_description, 'comment':comment_receive}
    
    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result':'success'})