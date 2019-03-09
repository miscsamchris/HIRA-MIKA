# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:51:26 2019

@author: TLSWM
"""

from flask import Flask,request,redirect,jsonify
app = Flask(__name__)
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests
import re
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_table(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()
def create_table(db_file):
    try:        
        conn = sqlite3.connect(db_file)
        cur =conn.cursor()
        try:
            cur.execute('''CREATE TABLE integrated (
    BEDNUMBER INTEGER PRIMARY KEY,
    NAME TEXT,
    AGE INTEGER, SEX TEXT, DIAGNOSIS TEXT,LAM TEXT,LAN TEXT,
    BP NUMERIC (10,2), TEMP NUMERIC (10,2), HB NUMERIC (10,2));''')
        except Error as e:
            print(e)
        try:
            cur.execute('''CREATE TABLE liveEntry (
    BEDNUMBER INTEGER,
    NAME TEXT,
    AGE INTEGER, SEX TEXT, DIAGNOSIS TEXT,LAM TEXT,LAN TEXT);''')
        except Error as e:
            print(e)
        try:
            cur.execute('''CREATE TABLE bedinfo (
    BEDNUMBER INTEGER PRIMARY KEY,
         TEXT,
    AGE INTEGER, SEX TEXT, DIAGNOSIS TEXT,LAM TEXT,LAN TEXT);''')
        except Error as e:
            print(e)
    except Error as e:
        print(e)
    finally:
        conn.close()
def userentry(data,mode=None):
    if mode==None:
        return dataentry(data["bedno"],data["name"],data["age"],data["sex"],data["diag"],data["lam"],data["lan"])
    else:
        return dataupdate(data["bedno"],data["name"],data["age"],data["sex"],data["diag"],data["lam"],data["lan"])
def recordentry(data,mode=None):
    if mode==None:
        return recordsentry(data["bedno"],data["name"],data["age"],data["sex"],data["diag"],data["lam"],data["lan"],data["bp"],data["hb"],data["temp"])
    else:
        return recordupdate(data["bedno"],data["name"],data["age"],data["sex"],data["diag"],data["lam"],data["lan"],data["bp"],data["hb"],data["temp"])

def dataentry(bedno,name,age,sex,diag,lam,lan,tn="liveEntry"):
    conn = sqlite3.connect("database.db")
    qry="insert into "+tn+" values(?,?,?,?,?,?,?);"
    try:
        cur=conn.cursor()
        cur.execute(qry, (int(bedno),name,int(age),sex,diag,lam,lan))
        conn.commit()
        print ("one record added successfully")
        conn.close()
        return True
    except:
        print("error in operation")
        conn.rollback()
        conn.close()
        return False
def dataupdate(bedno,name,age,sex,diag,lam,lan,tn="bedinfo"):
    conn = sqlite3.connect("database.db")
    if dataentry(bedno,name,age,sex,diag,lam,lan,tn)==True:
        return True
    else:
        qry="update "+tn+" set NAME=?,AGE=?,SEX=?,DIAGNOSIS=?,LAM=?,LAN=? where BEDNUMBER=?;"
        try:
            cur=conn.cursor()
            cur.execute(qry, (name,int(age),sex,diag,lam,lan,int(bedno)))
            conn.commit()
            print ("one record Edited successfully")
            conn.close()
            return True
        except Error as e:
            print(e)
            conn.rollback()
            conn.close()
            return False
def recordsentry(bedno,name,age,sex,diag,lam,lan,bp,hb,temp,tn="integrated"):
    conn = sqlite3.connect("database.db")
    qry="insert into "+tn+" values(?,?,?,?,?,?,?,?,?,?);"
    try:
        cur=conn.cursor()
        cur.execute(qry, (int(bedno),name,int(age),sex,diag,lam,lan,float(bp),float(hb),float(temp)))
        conn.commit()
        print ("one record added successfully")
        conn.close()
        return True
    except:
        print("error in operation")
        conn.rollback()
        conn.close()
        return False
def recordupdate(bedno,name,age,sex,diag,lam,lan,bp,hb,temp,tn="integrated"):
    conn = sqlite3.connect("database.db")
    if recordsentry(bedno,name,age,sex,diag,lam,lan,bp,hb,temp,tn)==True:
        return True
    else:
        qry="update "+tn+" set NAME=?,AGE=?,SEX=?,DIAGNOSIS=?,LAM=?,LAN=?,BP=?,HB=?,TEMP=? where BEDNUMBER=?;"
        try:
            cur=conn.cursor()
            cur.execute(qry, (name,int(age),sex,diag,lam,lan,float(bp),float(hb),float(temp),int(bedno)))
            conn.commit()
            print ("one record Edited successfully")
            conn.close()
            return True
        except Error as e:
            print(e)
            conn.rollback()
            conn.close()
            return False
@app.route('/')
def hello():
    return "Hello World!"
@app.route('/upload-data/',methods = ['POST', 'GET'])  
def getdata():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        diag = request.form['diag']
        bedno = request.form['bedno']
        lam = request.form['lam']
        lan = request.form['lan']
    else:
        name = request.args.get('name')
        age = request.args.get('age')
        sex = request.args.get('sex')
        diag = request.args.get('diag')
        bedno = request.args.get('bedno')
        lam = request.args.get('lam')
        lan = request.args.get('lan')
    if userentry({"bedno":bedno,"name":name,"age":age,"sex":sex,"diag":diag,"lam":lam,"lan":lan}):
        userentry({"bedno":bedno,"name":name,"age":age,"sex":sex,"diag":diag,"lam":lam,"lan":lan},"A")
        return "Data entry done"
    else:
        return "Data entry Not done"
@app.route('/upload-integrated/',methods = ['POST', 'GET'])  
def getentiredata():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        diag = request.form['diag']
        bedno = request.form['bedno']
        lam = request.form['lam']
        lan = request.form['lan']
        bp = request.form['bp']
        hb = request.form['hb']
        temp = request.form['temp']
    else:
        name = request.args.get('name')
        age = request.args.get('age')
        sex = request.args.get('sex')
        diag = request.args.get('diag')
        bedno = request.args.get('bedno')
        lam = request.args.get('lam')
        lan = request.args.get('lan')
        bp = request.args.get('bp')
        hb = request.args.get('hb')
        temp = request.args.get('temp')
    if recordentry({"bedno":bedno,"name":name,"age":age,"sex":sex,"diag":diag,"lam":lam,"lan":lan,"bp":bp,"hb":hb,"temp":temp}):
        return "Data entry done"
    else:
        recordentry({"bedno":bedno,"name":name,"age":age,"sex":sex,"diag":diag,"lam":lam,"lan":lan,"bp":bp,"hb":hb,"temp":temp},"A")
        return "Data entry Not done"
@app.route('/getinfoonbed/<string:bedno>/')
def dbinfo(bedno):
    db=sqlite3.connect('database.db')
    sql="SELECT * from integrated where BEDNUMBER ="+bedno+" ;"
    cur=db.cursor()
    cur.execute(sql)
    records=[]
    while True:
        record=cur.fetchone()
        if record==None:
            break
        records=record
    db.close()
    return jsonify(dict(zip(["bedno","name","age","sex","diag","lam","lan","bp","hb","temp"],records)))    
@app.route('/diseaseinfo/<string:topic>/')
def scraperdisease(topic):
    link="https://www.google.co.in/search?q="
    link+=topic
    request=requests.get(link)
    bs=BeautifulSoup(request.content,"html.parser")
    s=bs.find_all("div")
    nbs=BeautifulSoup(str(s[22]),"html.parser")
    s=nbs.find_all("div")
    return str(s[10])
@app.route('/medicineinfo/<string:topic>/')
def scrapermed(topic):
    topic=topic.split(" ")
    for i in topic:
        if i not in ["of","at","from","to"]:
            i=i.capitalize()
        else:
            i=i
    topic="_".join(topic)
    link="https://en.wikipedia.org/wiki/"
    link+=topic
    request=requests.get(link)
    bs=BeautifulSoup(request.content,"html.parser")
    s=bs.find_all("p")
    string=" "
    for i in s:
        if len(string)<300:
            string+=i.getText()
    string=re.sub(r"\[[0-9]*\]"," ",string)
    return string
if __name__ == '__main__':
    create_connection("database.db")
    app.run(debug=True, host='10.177.7.168', port="5000")