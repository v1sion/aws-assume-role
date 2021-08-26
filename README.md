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
Usage: aws-assume-role.py [OPTIONS] ACCOUNT ROLE

  Assume role

Arguments:
  ACCOUNT  [required]
  ROLE     [required]

Options:
  --aws-profile TEXT
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.
```

