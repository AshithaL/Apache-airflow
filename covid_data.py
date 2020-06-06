import csv
import json
import requests
import datetime
import cred as cred
from google.cloud import bigquery

def fetch_covid_data():
    """
    Fecthing covid data
    :return: No of row count
    """
    count = 0

    get_request = requests.get('https://api.covidindiatracker.com/state_data.json')
    url_data = get_request.text
    data = json.loads(url_data)
    covid_data = [['date', 'state', 'number_of_cases']]
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    for state in data:
        covid_data.append([date, state.get('state'), state.get('aChanges')])
        count += 1
    with open(cred.filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(covid_data)
    return count

def load_data():
    """
    Loading data to big query table
    :return: Output rows
    """
    dataset_ref = cred.client.dataset(cred.dataset_id)
    table_ref = dataset_ref.table(cred.table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    with open(cred.filename, "rb") as file:
        job_conf = cred.client.load_table_from_file(file, table_ref, job_config=job_config)

    job_conf.result()  # Waits for table load to complete.
    print("Loaded {} rows into {}:{}.".format(job_conf.output_rows, cred.dataset_id, cred.table_id))

    return job_conf.output_rows

def read_the_data(**kwargs):
    """
    Reading data to get the percentage of upload
    :param kwargs: Task ids
    :return: percentage
    """
    ti = kwargs['ti']
    v1 = ti.xcom_pull(task_ids='load_data')
    count = ti.xcom_pull(task_ids='fetch_data')
    print("percentage = {}".format((v1/count)*100))