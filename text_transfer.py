from pymongo import MongoClient
import time
import pika
try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")
#creating database connection instance
db = conn.database
#creating new database collection
collection = db.textsummary
with collection.watch() as stream:
	while stream.alive:
		change = stream.try_next()
		if change is not None:
			print("data not interested")
			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			#print(change)
			channel = connection.channel()
			message = change["fullDocument"]["message"]
			print("\n\n\n")
			print("In the message queue")
			print("inserted data",message)
			print("\n\n\n")
			channel.queue_declare(queue='hello')
			channel.basic_publish(exchange='',routing_key='hello',body=message)
			#print("Emitting Change: " + change['_id']['_data'])
			#sqs.send_message(
			#	QueueUrl=queue_url['QueueUrl'],
			#	MessageBody=get_insert_val(change['fullDocument'])
			#)
		# setting up message queue

			connection.close()
		time.sleep(10)
