#!/usr/bin/env python3
import boto3

def terminate_instance(): 
	try: 
		a=input("Enter instance id:")
		ec2_client = boto3.client("ec2", region_name="us-east-1")
		ec2_client.terminate_instances(InstanceIds=[a])
		print("Instance " +a+ " was successfully terminated!") 
	except Exception as ex: 
		print(ex) 

terminate_instance()


