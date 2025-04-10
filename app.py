import json
import boto3

def lambda_handler[event, context]:
client - boto3.client['ec2']
response = client.run_instances[
imageid-'ami-00a929b66ed6e0de6',
instancetype='t2.micro',
keyname-'key',
maxcount=1,
mincount=1
