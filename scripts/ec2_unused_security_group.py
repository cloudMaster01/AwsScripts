# Script to find all security groups not used by EC2 in a single AWS Region

import boto3

if __name__ == "__main__":
    ec2 = boto3.client("ec2")

    used_SG = set()

    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for sg in instance["SecurityGroups"]:
                used_SG.add(sg["GroupId"])

    response = ec2.describe_security_groups()
    total_SG = [sg["GroupId"] for sg in response["SecurityGroups"]]
    unused_SG = set(total_SG) - used_SG

    print(f"Total Security Groups: {len(total_SG)}")
    print(f"Used Security Groups: {len(used_SG)}\n")
    print(f"Unused Security Groups: {len(unused_SG)} compiled in the following list:")
    print(f"{list(unused_SG)}")
