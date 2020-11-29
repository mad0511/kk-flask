from flask import Flask,render_template,request,redirect,url_for
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    #open and read the file after the appending:
    silver_rate = open("silver_rate.txt", "r").read()
    gold_rate = open("gold_rate.txt", "r").read()
    tfourkgold = round((int(gold_rate) * 91.6)/100,2)
    ttkgold = round((int(tfourkgold)* 91.6)/100,2)
    
    return render_template("index.html",gold_rate=gold_rate,silver_rate=silver_rate,tfourkgold=tfourkgold,ttkgold=ttkgold)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/estimator',methods=['GET','POST'])
def estimator():
    try:
        try:
            username = request.form['username']
            password = request.form['password']
        except:
            pass
        try:
            key = request.args['key']
        except:
            pass
        if (username == "kkgoldmart@admin.com" and password == "vibin") or key == "kkgoldmart24kgold&silver":
            #open and read the file after the appending:
            silver_rate = open("silver_rate.txt", "r").read()
            gold_rate = open("gold_rate.txt", "r").read()
            tfourkgold = round((int(gold_rate) * 91.6)/100,2)
            ttkgold = round((int(tfourkgold)* 91.6)/100,2)
        
            return render_template("estimator.html",gold_rate=gold_rate,silver_rate=silver_rate,tfourkgold=tfourkgold,ttkgold=ttkgold)
        else:
            return render_template("login.html")
    except:
        return render_template("login.html")


@app.route('/changeRate',methods=['GET','POST'])
def changeRate():
    grate = request.form['grate']
    srate = request.form['srate']
    f = open("gold_rate.txt", "w")
    f.write(f"{grate}")
    f.close()
    f = open("silver_rate.txt", "w")
    f.write(f"{srate}")
    f.close()
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True,port=8081)