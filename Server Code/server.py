# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:51:26 2019

@author: TLSWM
"""

from flask import Flask,request,redirect
app = Flask(__name__)
import sqlite3
from sqlite3 import Error
 
 
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
            cur.execute('''CREATE TABLE histbiodata (
    BEDNUMBER INTEGER,
    NAME TEXT,
    BP INTEGER, TEMP INTEGER, HEART INTEGER);''')
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
    NAME TEXT,
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
if __name__ == '__main__':
    create_connection("database.db")
    app.run(debug=True, host='10.177.7.168', port="5000")