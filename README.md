# Background
Your company needs a scalable solution to automatically generate thumbnails for images uploaded to an S3 bucket. The thumbnails should be resized to 200x200 pixels and stored in a separate "thumbnails" S3 bucket.

This serverless project uses a lambda built with Python and a lambda layer (Pillow) for image manipulation.

# Requirements
- npm
- serverless
- python3.9

# Deployment
- serverless deploy --stage example

# AWS Security Foundations

https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html

# To do
## Serverless Unit Tests with Python
https://dev.to/charlesco/testing-serverless-python-applications-with-serverless-offline-pytest-5en9