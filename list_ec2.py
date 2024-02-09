# import json
# import boto3

# region="ap-south-1"

# instances = ['i-01d11472648a8df45']

# def lambda_handler(event, context):
#     #TODO IMPLEMENT
#     ec2 = boto3.client('ec2', region_name=region)
#     ec2.stop_instances(InstanceIds=instances)
#     print ('stop your instances: ' + str(instances))

import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    
    # Define the tag key and value to filter instances
    tag_key = 'nightUsage'
    tag_value = '0'
    
    # Retrieve instances with the specified tag value
    response = ec2.describe_instances(Filters=[
        {
            'Name': f'tag:{tag_key}',
            'Values': [tag_value]
        }
    ])
    
    # Extract instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Instances stopped: {instance_ids}")
    else:
        print("No instances found with the specified tag value.")