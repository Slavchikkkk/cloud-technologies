#!/usr/bin/env python3
import boto3

def upload(): 
	try: 
		a=str(input("Enter s3 bucket name:"))
		file_name=str(input("Enter path to file:"))
		s3_file_name=str(input("Enter what the file will be called:"))
		s3_client = boto3.client('s3')
		s3_client.upload_file(Filename=file_name,Bucket=a,Key=s3_file_name)
		print("File" +file_name+ " was successfully uploaded!") 
	except Exception as ex: 
		print(ex) 

upload()


