#!/usr/bin/env python3
import boto3
import os

def create_key_pair():
    try:
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        a=input("Enter the name of key pair:")
        key_pair = ec2_client.create_key_pair(KeyName=a)
        private_key = key_pair["KeyMaterial"]
        with os.fdopen(os.open("/tmp/"+ a +".pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
            handle.write(private_key)
        print(a +".pem was succesfully created!")
    except Exception as ex:
        print(ex)

create_key_pair()




