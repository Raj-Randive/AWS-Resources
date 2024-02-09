import boto3

# Create an EC2 client
ec2 = boto3.client("ec2")

# Retrieve all instances
response = ec2.describe_instances()

# Extract instance information from the response
instances = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instances.append(
            {
                "InstanceId": instance["InstanceId"],
                "InstanceType": instance["InstanceType"],
                "State": instance["State"]["Name"],
            }
        )

# Print instance information
for instance in instances:
    print(
        f"Instance ID: {instance['InstanceId']}, Instance Type: {instance['InstanceType']}, State: {instance['State']}"
    )
