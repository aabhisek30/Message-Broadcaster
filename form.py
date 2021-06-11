from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, validators
from pymongo import MongoClient
import mysql.connector
from mysql.connector import errorcode


app = Flask(__name__)

class message(Form):
    messagetext = TextAreaField('message',[validators.Length(min = 1,max = 1000)])

@app.route('/',methods=['GET','POST'])
def register():
    form = message(request.form)
    if request.method == "POST" and form.validate():
        print("data from gui")
        print(form.messagetext.data)
        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")
        #creating database connection instance
        db = conn.database
        #creating new database collection
        collection = db.textsummary
        Text1 = {
        "message":form.messagetext.data
        }
        rec_id1 = collection.insert_one(Text1)

        #printing the inserted data
        cursor = collection.find()

        #taking data from mangodb
        data = []
        for record in cursor:
            print("taken from mangodb database")
            data.append(record["message"])
            print(record["message"])

        #Deleting from database at the end of iteration
        #x = collection.delete_many({})
        return redirect(url_for('script_output'))
    return render_template('register.html',form = form)



@app.route('/output')
def script_output():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abhi1998",
    database="text_data"
    )

    #creating database

    # Cursor setup
    cursor_sq = mydb.cursor()
    result = []
    query = "select * from text"
    cursor_sq.execute(query)
    print("printing on command prompt")
    for r in cursor_sq.fetchall():
        result.append(r)
    return render_template('output.html',response = result)

if __name__ == '__main__':
    app.run(debug=True)
