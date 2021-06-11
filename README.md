# Message-Broadcaster

## Tools and libaries

1. Web Framework – Flask
2. NoSQL Database – MongoDb
3. Messaging Queuing system – Rabbit MQ
4. Relational Database – MySQL
5. MongoDb connector – Pymongo
6. MySQL connector – MySQL
7. Message Queuing system – pika

## Architecture

1. System Architecture
![system architecture](https://user-images.githubusercontent.com/67454437/121729031-a350ea80-cb0b-11eb-9cdf-e69c680fd692.png)
2. Input Data Flow
![Input_Data](https://user-images.githubusercontent.com/67454437/121729092-b499f700-cb0b-11eb-9817-fe54d68eeecf.png)
3. Output Data Flow
![Output](https://user-images.githubusercontent.com/67454437/121729140-c11e4f80-cb0b-11eb-97eb-6cb3c30276d8.png)

## File details-


### Register.html - It is used to render input from text box to the form.py

### Form.py 

### Input part –

1. It takes data from Register.html by using flask
2. It connects to MongoDb database using pymongo
3. write data read from html page to textsummary collection of database named database

### Output part -

1. Connect to MySQL by using MySQL connector
2. Read data from table named text of database named text_data
3. Redirect message to output.html

### Text_transfer.py -

1. It set up a message queue name “hello”
2. It is constantly watching mongodb database
3. As soon as there is change in mongodb database, text_transfer read it and send to “hello” queue


### Recieve.py -

1. This file is constantly running
2. It is at the receiving end of the hello message queue
3. It reads data from message queue
4. It writes data to MySQL database

### Output.html -

1. It writes data to new page.

File running sequence

1. recieve.py
2. text_transfer.py
3. form.py

For more detail, check out file Program_Flow.pdf
 

