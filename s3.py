import boto3
import logging
from botocore.exceptions import ClientError
import os


class S3Helper:
    def __init__(self):
        self.bucket_name = 'fvcchw1'
        self.url = 'https://s3.ir-thr-at1.arvanstorage.com'
        self.access_key_id = '3484c9e5-aae7-496e-b7e2-0fd86f665ca4'
        self.secret_access_key = '3d9c29f8e52c3337d56d29ada8df56cfb02a1027'

    def upload_file(self, image, image_id):
        logging.basicConfig(level=logging.INFO)

        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url=self.url,
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key
            )

        except Exception as exc:
            logging.error(exc)
        else:
            try:
                bucket = s3_resource.Bucket(self.bucket_name)
                object_name = f'{image_id}.jpg'

                bucket.put_object(
                    ACL='private',
                    Body=image,
                    Key=object_name
                )
                print("file uploaded")
            except ClientError as e:
                logging.error(e)

    def download_file(self, image_id):
        logging.basicConfig(level=logging.INFO)

        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url=self.url,
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key
            )
        except Exception as exc:
            logging.error(exc)
        else:
            try:
                bucket = s3_resource.Bucket(self.bucket_name)

                object_name = f'{image_id}.jpg'
                download_path = os.path.join(os.getcwd(), 'images', object_name)

                bucket.download_file(
                    object_name,
                    download_path
                )
                print("image downloaded")
            except ClientError as e:
                logging.error(e)
        return image_id

    def remove_file(self, image_id):
        file_name = f'{image_id}.jpg'
        file_path = os.path.join(os.getcwd(), 'images', file_name)
        os.remove(file_path)


if __name__ == '__main__':
    S3Helper().remove_file(18)
