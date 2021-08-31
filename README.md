# aws-assume-role

Helper script that assumes an aws role and exports the credentials as environment variables.
Can also discard the current role by unsetting the environment variables.

## How to assume a role

```sh
eval `./aws-assume-role.py assume-role <account-id> <role-name>`
```

### Install

```sh
pip install -r requirements.txt
```

### Usage

```sh
Usage: aws-assume-role.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  assume-role   Assume AWS role
  discard-role  Discard current role
```
