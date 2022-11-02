from importlib.metadata import entry_points
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws-assume-role",
    version="0.1.0",
    author="v1sion",
    author_email="andremomorais@gmail.com",
    description="Prints AWS account name from account id",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        'boto3==1.18.28',
        'typer==0.3.2',
    ],
    entry_points={"console_scripts": [
        "aws-assume-role = aws_assume_role.main:app"]},
)
