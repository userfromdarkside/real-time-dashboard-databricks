import boto3
import json
import random
import time
import uuid
from faker import Faker
from dataclasses import dataclass, field
from botocore.exceptions import ClientError

s3_resource = boto3.resource('s3')

bucket_name = '********'  
# check if the s3 bucket exists
def bucket_exists(bucket_name):
    try:
        s3_resource.meta.client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        print(f"Bucket '{bucket_name}' does not exist or is inaccessible.")
        return False

faker = Faker()
currencies = ['VND', 'USB', 'AUD']

@dataclass
class Transaction:
    username: str = field(default_factory=faker.user_name)
    currency: str = field(default_factory= lambda: currencies[random.randint(0,len(currencies)-1)])
    amount: str = field(default_factory=lambda: random.randint(100, 200000))
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    city: str = field(default_factory=faker.city)
    nation: str = field(default_factory=faker.country)

    def serialize(self):
        return dict(
            {
                "username": self.username,
                "currency": self.currency,
                "amount": self.amount,
                "transaction_id": self.transaction_id,
                "city": self.city,
                "nation": self.nation
            }
        )

def Producer(file_string):
    filename = file_string
    with open(filename, 'a') as file:
        json.dump(Transaction().serialize(), file)
        file.write(",\n")
    s3_resource.Bucket(bucket_name).upload_file(Filename=filename, Key=filename)

for i in range(100): # change to a lower number for testing
    Producer(f'transactions_{str(uuid.uuid4())}.json')
    print('iteration:', i)
    time.sleep(3)