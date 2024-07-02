import boto3
import os, uuid
import PIL
from PIL import Image
from io import BytesIO

s3_client = boto3.client('s3')

import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((200, 200))  # As per requirements
        image.save(resized_path)

def s3_thumbnail_generator(event, context):
    
    # Read event and collect bucket name, key of image uploaded and set paths

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    upload_path = '/tmp/resized-{}'.format(key)
    
    try:
        logger.info("Download File: "+ bucket + " - " + key + " - " + download_path)
        s3_client.download_file(bucket, key, download_path)
        logger.info("Resize Image: "+ download_path + " - " + upload_path)
        resize_image(download_path, upload_path)
        logger.info("Upload Image: "+ upload_path + " - " + os.environ['THUMBNAIL_BUCKET'] + " - " + key)
        s3_client.upload_file(upload_path, os.environ['THUMBNAIL_BUCKET'], key)
        logger.info("Upload completed - "+ key +" completed")
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_stack(limit=10))

   