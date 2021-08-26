#!python
import typer
import boto3
from typing import Optional

__version__ = "0.1.0"

app = typer.Typer(add_completion=False)


@app.command()
def assume_role(
    account: str = typer.Argument(..., help="AWS account id"),
    role: str = typer.Argument(..., help="AWS role to assume"),
    aws_profile: Optional[str] = typer.Argument(None, help="AWS configuration profile"),
):
    """Assume AWS role"""

    session = boto3.Session()
    if aws_profile:
        session = boto3.Session(profile_name=aws_profile)

    sts_client = session.client("sts")
    assumed_role_object = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{account}:role/{role}",
        RoleSessionName=f"{role}-session",
    )
    credentials = assumed_role_object["Credentials"]
    print(
        f"export AWS_ACCESS_KEY_ID={credentials['AccessKeyId']}\nexport AWS_SECRET_ACCESS_KEY={credentials['SecretAccessKey']}\nexport AWS_SESSION_TOKEN={credentials['SessionToken']}"
    )


if __name__ == "__main__":
    app()
