#!/usr/bin/python

from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
# "message-topic" is the topic name
# data is the message send
data = {'msgs' : hello everyone}
producer.send('message-topic', value=data)
producer.flush()






