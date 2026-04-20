from langchain.tools import tool
import subprocess

def run_aws(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or result.stderr or "No results"


@tool
def get_s3_buckets(input: str = "list") -> str:
    """List all S3 buckets in the AWS account"""
    return run_aws(["aws", "s3", "ls"])


@tool
def get_ec2_instances(input: str = "list") -> str:
    """List all EC2 instances with state"""
    return run_aws([
        "aws", "ec2", "describe-instances",
        "--query", "Reservations[].Instances[].{ID:InstanceId,State:State.Name}",
        "--output", "table"
    ])


@tool
def get_vpcs(input: str = "list") -> str:
    """List all VPCs in the AWS account"""
    return run_aws([
        "aws", "ec2", "describe-vpcs",
        "--query", "Vpcs[].{ID:VpcId,CIDR:CidrBlock}",
        "--output", "table"
    ])


@tool
def get_cloudwatch_alarms(input: str = "list") -> str:
    """List all CloudWatch alarms"""
    return run_aws([
        "aws", "cloudwatch", "describe-alarms",
        "--query", "MetricAlarms[].{Name:AlarmName,State:StateValue}",
        "--output", "table"
    ])
