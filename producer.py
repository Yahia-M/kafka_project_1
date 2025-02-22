from kafka import KafkaProducer
from pymongo import MongoClient
import json

# MongoDB Atlas connection
mongo_uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client['<dbname>']
collection = db['<collectionname>']

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Read data from MongoDB and produce to Kafka
for document in collection.find():
    producer.send('<kafka_topic>', document)
    print(f"Produced: {document}")

producer.flush()