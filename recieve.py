import pika, sys, os
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi1998",
        database="text_data"
        )

       # Cursor setup
        cursor_sq = mydb.cursor()
        #inserting into mysql DATABASE
        print(body.decode('ascii'))
        add_text = "INSERT INTO text(text_message) VALUES ('{}')".format(body.decode('ascii'))
        cursor_sq.execute(add_text)

        print("\n\n\n")
        print("Data written to mysql database")
        print("\n\n\n")

        # Make sure data is committed to the database
        mydb.commit()

        query = "select * from text"

        cursor_sq.execute(query)

        print("printing on command prompt")
        for result in cursor_sq.fetchall():
            print(result)
            print(result[0])
            print(result[1])
        cursor_sq.close()
        mydb.close()




    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
