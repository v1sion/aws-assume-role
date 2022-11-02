#!python
import typer
import boto3
from typing import Optional

__version__ = "0.2.0"

app = typer.Typer(add_completion=False)


@app.command()
def assume_role(
    role: str = typer.Argument(..., help="AWS role to assume"),
    account: str = typer.Argument(..., help="AWS account id"),
    token_code: Optional[str] = typer.Option(None, help="AWS mfa token"),
    serial_number: Optional[str] = typer.Option(None, help="AWS token id"),
    external_id: Optional[str] = typer.Option(None, help="AWS external id"),
    profile: Optional[str] = typer.Option(
        None, help="AWS configuration profile"),
):
    """Assume AWS role"""

    session = boto3.Session()
    if profile:
        session = boto3.Session(profile_name=profile)
    sts_client = session.client("sts")

    if token_code or serial_number:
        assumed_role_object = sts_client.assume_role(
            RoleArn=f"arn:aws:iam::{account}:role/{role}",
            RoleSessionName=f"{role}-session",
            TokenCode=token_code,
            SerialNumber=serial_number,
        )
    elif external_id:
        assumed_role_object = sts_client.assume_role(
            RoleArn=f"arn:aws:iam::{account}:role/{role}",
            RoleSessionName=f"{role}-session",
            ExternalId=external_id,
        )
    else:
        assumed_role_object = sts_client.assume_role(
            RoleArn=f"arn:aws:iam::{account}:role/{role}",
            RoleSessionName=f"{role}-session",
        )

    credentials = assumed_role_object["Credentials"]
    print(
        f"export AWS_ACCESS_KEY_ID={credentials['AccessKeyId']}\nexport AWS_SECRET_ACCESS_KEY={credentials['SecretAccessKey']}\nexport AWS_SESSION_TOKEN={credentials['SessionToken']}"
    )


@app.command()
def discard_role():
    """Discard current role"""

    print(
        f"unset AWS_ACCESS_KEY_ID\nunset AWS_SECRET_ACCESS_KEY\nunset AWS_SESSION_TOKEN"
    )


if __name__ == "__main__":
    app()
