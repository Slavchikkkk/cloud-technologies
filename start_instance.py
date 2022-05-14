#!/usr/bin/env python3
import boto3

def stop_instance(): 
	try: 
		a=input("Enter instance id:")
		ec2_client = boto3.client("ec2", region_name="us-east-1")
		ec2_client.start_instances(InstanceIds=[a])
		print("Instance " +a+ " was successfully started!") 
	except Exception as ex: 
		print(ex) 

stop_instance()


