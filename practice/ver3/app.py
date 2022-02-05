from flask import render_template, Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://test:test@54.180.117.207', 27017)
db = client.ver2    #ver2라는 이름의 db를 만든다!


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/memo/create', methods=['POST'])
def post_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    memoes = {'title':title_receive,'content':content_receive}

    db.book.insert_one(memoes)

    return jsonify({'result':'success'})

@app.route('/api/memo/list',methods=['GET'])
def show_memo():
    result=list(db.book.find({}))
    results=[]
    for i in result:
        i['_id'] = str(i['_id'])
        results.append(i)
    return jsonify({'result':'success','memo_list':results})

@app.route('/api/memo/delete', methods=['POST'])
def delete_memo():
    _id_receive = request.form['_id_give']
    db.book.delete_one({'_id': ObjectId(_id_receive)})

    return jsonify({'result':'success'})

@app.route('/api/memo/modify',methods=['POST'])
def edit_memo():
    _id_receive = request.form['_id_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    db.book.update_one({'_id':ObjectId(_id_receive)},{'$set':{'title':title_receive}})
    db.book.update_one({'_id':ObjectId(_id_receive)},{'$set':{'content':content_receive}})
    return jsonify({'result':'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

