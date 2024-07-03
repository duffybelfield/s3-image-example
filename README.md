# Background
Your company needs a scalable solution to automatically generate thumbnails for images uploaded to an S3 bucket. The thumbnails should be resized to 200x200 pixels and stored in a separate "thumbnails" S3 bucket.

This serverless project uses a lambda built with Python and a lambda layer (Pillow) for image manipulation.

# Requirements
- npm
- serverless
- python3.9

# External Cloudformation templates required within the account
- vpc3az
- - Defines the vpc, routes, nats etc.
- vpc-s3-endpoint
- - Defines vpc endpoint for s3 so that requests to s3 API are completed over an internet network
- alert
- - Deploys SNS topics
- slack
- - Deploys configuration to push SNS notifications to slack

# Cloudformation templates
- Alarms
- - Example Lambda alarms that can be used
- Buckets
- - Buckets required for example with bucket policies
- IAM
- - Minimal permission role and policy


# Deployment
- serverless deploy --stage example

# AWS Security Foundations

https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html

# To do
## Serverless Unit Tests with Python
https://dev.to/charlesco/testing-serverless-python-applications-with-serverless-offline-pytest-5en9