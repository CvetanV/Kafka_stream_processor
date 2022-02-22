# importing the required libraries
from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd


# initializing the Kafka producer
data_producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)

# Read data from the csv with Pandas
dataFrame = pd.read_csv("dataset.csv", sep=";")

# Transform dataframe to a dictionary
def to_dictionary(data):
    data.set_index("ID", drop=True, inplace=True)
    dictionary = data.to_dict(orient="index")
    return dictionary


dict_data = to_dictionary(dataFrame)

# Read dictionary items
for item in dict_data.items():
    data = {"Weather Data": item}
    data_producer.send("weather_data1", value=data)
    print("Sent", data)
    sleep(1)
