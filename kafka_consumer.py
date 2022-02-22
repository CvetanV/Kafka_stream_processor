# importing the required modules
from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient

# generating the Kafka Consumer
data_consumer = KafkaConsumer(
    "weather_data1",  # tag of the sent data
    bootstrap_servers=["localhost : 9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-group",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)

# Connect to mongo db and colection
mongo_db_client = MongoClient("localhost:27017")
mongo_collection = mongo_db_client.kafka_db.kafka_weather_data

# iterate through the data sent by the producer
for message in data_consumer:
    message = message.value
    mongo_collection.insert_one(message)
    print(message, " added to ", mongo_collection)
