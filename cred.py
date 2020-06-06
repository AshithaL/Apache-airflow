"This file contains Google related credentials"

import os
import datetime
from google.cloud import bigquery

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nineleaps/Downloads/pure-environs-279206-32615e0b1a7f.json"
client = bigquery.Client()
filename = '/home/nineleaps/Downloads/covid_data_{}.csv'.format(
    datetime.datetime.today().strftime('%Y-%m-%d'))

dataset_id = 'ashithal'
table_id = 'airflow'