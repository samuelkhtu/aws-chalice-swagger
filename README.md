# aws-chalice-template

AWS Chalice Starter Template with Build-in Swagger UI Support

## AWS Chalice

[AWS Chalice](https://aws.github.io/chalice/) is a micoservice framework for writing serverless appications in python. User can quickly create and deploy applications to AWS environment.

-   [AWS Chalice Tutorial & Documentation](https://aws.github.io/chalice/tutorials/index.html)

## What is this project?

This project provides a ready-to-use template for your project. The biggest value-add is the built-in Swagger UI.

## Prerequisite

-   [Visual Studio Code](https://www.python.org/downloads/release/python-381/)
-   [Python](https://www.python.org/downloads/release/python-381/) >= 3.8.1
-   [AWS Credential](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Install

Clone Git Repository to your local file system

```bash

git clone https://github.com/samuelkhtu/aws-chalice-template.git

```

Navigate to the aws-chalice-template folder

```bash

cd aws-chalice-template

```

Setup Python Virtual Environment

```bash

python -m venv .venv


```

Activate Python Virtual Environment

```bash

# Mac
source .venv/bin/Activate

# Window
source .venv/Scripts/Activate

```

Install Required Python Library

```bash

pip install -r requirements.txt

```

Deploy To AWS

```bash

❯ chalice deploy --no-autogen-policy

Updating lambda function: aws-chalice-template-dev
Updating rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-1::function:aws-chalice-template-dev
  - Rest API URL: https://...execute-api.us-east-1.amazonaws.com/dv/

```

> Node: Current issue [#1643](https://github.com/aws/chalice/issues/1643) prevent Chalice deploy to pick up `"autogen_policy": "False"` parameter correctly. Make sure to include `--no-autogen-policy` arguement

Copy & paste the URL from your terminal to your browser. You should see the familiar [Swagger UI](https://swagger.io/tools/swagger-ui/).

## Environment Setup

### Log Level

Log level is controlled by `ENV_LOG_LEVEL` environment variables. `.chalice\config.json`

-   CRITICAL
-   ERROR
-   WARNING
-   INFO
-   DEBUG
-   NOTSET

-   Reference: [logging level](https://docs.python.org/3/library/logging.html#levels)

### Custom IAM Role Policy

You can customize the IAM role policy with your project.

-   [AWS Chalice Document](https://aws.github.io/chalice/topics/configfile#iam-policy-file)
-   [AWS IAM Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
