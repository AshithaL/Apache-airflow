# Apache - Airflow
## Covid Pipeline 

## Requirements
- Apache Airflow
- Python version 3.6
- Google cloud platform

## Installation 
- mkdir airflow

- Set env variables
```
export AIRFLOW_HOME=~/airflow
```
## Install using pip
```
pip install apache-airflow
```
This creates: 
- airflow.cfg

File which contains defaults and other configuration settings.

For this project, set the executor as SequentialExecutor and dag examples to false.
- unittests.cfg

## Initialize the database
```
airflow initdb
```
- Creates airflow.db file
## Start the web server, default port is 8080
```
airflow webserver -p 8080
```
#start the scheduler
```
airflow scheduler
```
- Creates airflow-webserver.pid
### Go to localhost 8080- and select the dag file from home page.

## Dependencies
**Google cloud platform Bigquery**

pip install --upgrade google-cloud-bigquery

**Apache airflow**

pip install apache-airflow
## Google cloud platform
It is used for uploading data from local to google cloud platform via bigquery table.
- Create a new project and save the credentials.
- Create dataset and table with required fields.

## Files
The below mentioned file has the following

- cred.py - Google credentials file
- covid_data.py - Functionalties and loading data to big query table
- covid_dag.py - The pipeline workflow
- Tasks/tasks.py - The required tasks to run pipeline

## Run
```Tasks/run_tasks.py```

Save the required files to airflow/dags folder and run localhost:8080.

## How airflow looks

![Alt text](/home/nineleaps/Pictures/Image3.png?raw=true "Pipeline")

![Alt text](/home/nineleaps/Pictures/Image4.png?raw=true "Big query table")
