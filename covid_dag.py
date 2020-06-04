import csv
import json
import os
import requests
import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from google.cloud import bigquery

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nineleaps/Downloads/pure-environs-279206-32615e0b1a7f.json"
client = bigquery.Client()
filename = '/home/nineleaps/Downloads/covid_data_{}.csv'.format(
    datetime.datetime.today().strftime('%Y-%m-%d'))
dataset_id = 'ashithal'
table_id = 'airflow'

#default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'depends_on_past': False,
    'email': ['ashitha.l@nineleaps.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}
# Instantiating dag
dag = DAG(dag_id='covid_pipeline',
          default_args=default_args,
          description="Collecting covid data",
          schedule_interval=timedelta(days=1),
          )

def fetch_covid_data():
    
    "Fetch data from json"
    
    r = requests.get('https://api.covidindiatracker.com/state_data.json')
    r_data = r.text
    data = json.loads(r_data)
    count = 0
    covid_data = [['date', 'state', 'number_of_cases']]
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    for state in data:
        covid_data.append([date, state.get('state'), state.get('aChanges')])
        count += 1
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(covid_data)
    return count

def load_data(**kwargs):
    
    "Loading into bq table"
    
    bq_dataset_ref = client.dataset(dataset_id)
    bq_table_ref = bq_dataset_ref.table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, bq_table_ref, job_config=job_config)

    job.result()  # Waits for table load to complete.

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
    return job.output_rows

def read_data(**kwargs):
    
    "Calculating Percentage"

    t = kwargs['t']
    v1 = ti.xcom_pull(task_ids='load_data')
    count = ti.xcom_pull(task_ids='fetch_data')
    print("percentage = {}".format((v1/count)*100))

t1 = PythonOperator(task_id="fetch_data", python_callable=fetch_covid_data, dag=dag)

t2 = PythonOperator(task_id="load_data", python_callable=load_data, dag=dag)

t3 = PythonOperator(task_id="percentage", python_callable=read_data, provide_context=True, dag=dag)

t1 >> t2 >> t3
