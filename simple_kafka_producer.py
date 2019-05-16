#!/usr/bin/python

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
# "message-topic" is the topic name
# "Hello everyone" is the message send
producer.send('message-topic', b'Hello everyone')
producer.flush()


