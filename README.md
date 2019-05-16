# Kafka_Producer

pip install kafka-python

# Start ZooKeeper Server
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

By default Zookeeper is running on localhost:2181 and Kafka on localhost:9092.


# Creating Kafka Topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic message-topic
