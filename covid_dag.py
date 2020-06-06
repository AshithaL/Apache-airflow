"Dag file"

from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'depends_on_past': False,
    'email': ['ashitha.l@nineleaps.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}
dag = DAG(dag_id='covid',
          default_args=default_args,
          description="Collecting covid data",
          schedule_interval=timedelta(days=1),
          )

