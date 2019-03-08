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
        cur.execute('''CREATE TABLE histbiodata (
    BEDNUMBER INTEGER,
    name TEXT,
    BP INTEGER, TEMP INTEGER, HEART INTEGER);''')
        cur.execute('''CREATE TABLE LastuserDataabse (
    BEDNUMBER INTEGER,
    name TEXT,
    BP INTEGER, TEMP INTEGER, HEART INTEGER);''')

    except Error as e:
        print(e)
    finally:
        conn.close()
@app.route('/')
def hello():
    return "Hello World!"
@app.route('/upload-data/',methods = ['POST', 'GET'])  
def getdata():
    if request.method == 'POST':
        user = request.form['name']
    else:
       user = request.args.get('name')
    return "Hello {a}".format(a=user)
    
if __name__ == '__main__':
    create_connection("database.db")
    app.run(debug=True, host='10.177.7.168', port="5000")