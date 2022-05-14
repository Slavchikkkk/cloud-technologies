#!/usr/bin/env python3
import boto3

def create_instance():
	try:
		a=input("Enter name of instance:")
		ec2_client = boto3.client("ec2", region_name="us-east-1")
		instances = ec2_client.run_instances(
			ImageId="ami-0a8b4cd432b1c3063",
			MinCount=1,
			MaxCount=1,
			InstanceType="t2.micro",
			KeyName=a,
			SecurityGroups=['launch-wizard-1'])
		print("Instance with id "+ instances["Instances"][0]["InstanceId"] + " was successfully created!")
	except Exception as ex:
		print(ex)

create_instance()


