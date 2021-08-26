# aws-assume-role

Helper script that assumes an aws role and exports the credentials as env var

## How to run

```sh
eval `./aws-assume-role.py <account-id> <role-name>`
```

### Install

```sh
pip install -r requirements.txt
```

### Usage

```sh
Usage: aws-assume-role.py [OPTIONS] ACCOUNT ROLE [AWS_PROFILE]

  Assume AWS role

Arguments:
  ACCOUNT        AWS account id  [required]
  ROLE           AWS role to assume  [required]
  [AWS_PROFILE]  AWS configuration profile

Options:
  --help  Show this message and exit.

```
