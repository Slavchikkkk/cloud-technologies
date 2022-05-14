#!/usr/bin/env python3
import boto3

def create_s3(): 
	try: 
		a=str(input("Enter s3 bucket name:"))
		s3_client = boto3.client('s3')
		s3_client.create_bucket(Bucket=a)
		print("S3 " +a+ " was successfully created!") 
	except Exception as ex: 
		print(ex) 

create_s3()


