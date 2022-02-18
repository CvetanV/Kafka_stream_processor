# importing the required libraries
import pandas as pd
from time import sleep
from json import dumps
from kafka import KafkaProducer

# initializing the Kafka producer
data_producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],
                              value_serializer = lambda x:dumps(x).encode('utf-8')
                              )

# Read data from the csv with Pandas
df = pd.read_csv("dataset.csv", sep=';')

# Transform dataframe to a dictionary
def to_dictionary(df):
    df.set_index("ID", drop=True, inplace=True)
    dictionary = df.to_dict(orient="index")
    return dictionary
dict_data = to_dictionary(df)

# Read dictionary items
for item in dict_data.items():
    data = {'Weather Data': item}
    data_producer.send('weather_data1', value=data)
    print("Sent", data)
    #sleep(1)