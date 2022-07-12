from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os
app = Flask(__name__)

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

ca = certifi.where()
client = MongoClient(MONGODB_URL, tlsCAFile=ca)
db = client.MBTI

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/commentAction', methods=['POST'])
def commentAction():
    comment_receive = request.form['txt']
    print(comment_receive)
    doc={
        'comment_receive':comment_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '등록완료'})

@app.route('/getComment', methods=['GET'])
def getComment():
    # comment_receive = request.agrs.get['txt']
    all_comment = list(db.comment.find({},{'_id':False}))
    # for alls in all_comment:
    #     print(alls)
    print(all_comment)
    return jsonify({'msg': all_comment})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)