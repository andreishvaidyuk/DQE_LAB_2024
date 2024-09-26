import boto3
import pytest
import requests
from botocore import UNSIGNED
from botocore.config import Config
from google.cloud import storage
import allure


@pytest.fixture(scope='function')
def provide_config():
    config = {'prefix': '2024/01/01/KTLX/', 'gcp_bucket_name': "gcp-public-data-nexrad-l2",
              'aws_bucket_name': 'noaa-nexrad-level2',
              's3_anon_client': boto3.client('s3', config=Config(signature_version=UNSIGNED)),
              'gcp_storage_anon_client': storage.Client.create_anonymous_client()}
    return config


@pytest.fixture(scope='function')
def list_gcs_blobs(provide_config):
    config = provide_config
    blobs = config['gcp_storage_anon_client'].list_blobs(config['gcp_bucket_name'], prefix=config['prefix'])
    objects = [blob.name for blob in blobs]
    return objects


@pytest.fixture(scope='function')
def list_aws_blobs(provide_config):
    config = provide_config
    response = config['s3_anon_client'].list_objects(Bucket=config['aws_bucket_name'], Prefix=config['prefix'])
    objects = [content['Key'] for content in response['Contents']]
    return objects


@pytest.mark.posts
@allure.story("Count of posts Test")
def test_user_with_posts(provide_posts_data):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = provide_posts_data

    response = requests.get(url, params=params)
    posts = response.json()
    post_count = len(posts)
    assert post_count == 10, "Test failed! Expected 10 posts, but found {post_count} posts for user with Id=3."


@pytest.mark.hasdata
def test_data_is_presented_between_staging_raw():
    gcp_data_exists = list_gcs_blobs
    aws_data_exists = list_aws_blobs

    assert gcp_data_exists, f"No data found in GCP bucket"
    assert aws_data_exists, f"No data found in AWS bucket"
