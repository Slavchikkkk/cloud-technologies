#!/usr/bin/env python3
import boto3

def delete_s3(): 
	try: 
		a=str(input("Enter s3 bucket name:"))
		#попереднє видалення усіх файлів з бакету
		s3 = boto3.resource('s3')
		bucket = s3.Bucket(a)
		bucket.objects.all().delete()
		#видалення самого бакету
		s3_client = boto3.client('s3')
		s3_client.delete_bucket(Bucket=a)
		print("S3 " +a+ " was successfully deleted!") 
	except Exception as ex: 
		print(ex) 

delete_s3()


