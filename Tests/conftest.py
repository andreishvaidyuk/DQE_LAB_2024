import os
import sys
import pytest
import yaml
import psycopg2


@pytest.fixture(scope="session")
def connect_to_db_postgre():
    conn = psycopg2.connect(
        database="Everything_Sales",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )
    yield conn
    conn.close()


#@pytest.fixture(scope="session")
def smoke_tests_queries(config_name):
    module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
    parent_dir = os.path.dirname(module_dir)
    with open(os.path.join(parent_dir, 'Configs', config_name), 'r') as stream:
        config = yaml.safe_load(stream)
    return config['smoke_tests']


def critical_tests_queries(config_name):
    module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
    parent_dir = os.path.dirname(module_dir)
    with open(os.path.join(parent_dir, 'Configs', config_name), 'r') as stream:
        config = yaml.safe_load(stream)
    return config['critical_tests']


@pytest.fixture(scope='function')
def provide_posts_data():
    params = {
        "userId": 3
    }
    return params