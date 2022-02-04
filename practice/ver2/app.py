from flask import render_template, Flask, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.ver2    #ver2라는 이름의 db를 만든다!

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['POST'])
def post_memo():
    title_receive = request.form['memo_title']
    content_receive = request.form['memo_content']

    memoes = {'title':title_receive,'content':content_receive}

    db.book.insert_one(memoes)

    return jsonify({'result':'success','memoes':memoes})

@app.route('/memo',methods=['GET'])
def show_memo():
    result=list(db.book.find({},{'_id':0}))
    return jsonify({'result':'success','memo_list':result})

@app.route('/delete', methods=['POST'])
def delete_memo():
    delete = request.form['target']
    db.book.delete_one({'title': delete})

    return jsonify({'result':'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

