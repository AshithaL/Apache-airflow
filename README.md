#Covid Pipeline
==

Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

## Requirements
Apache Airflow
Python version 3.6
Google cloud platform

## Installation 
mkdir airflow

but you can lay foundation somewhere else if you prefer
(optional)
export AIRFLOW_HOME=~/airflow

## Install from pypi using pip

```
pip install apache-airflow
```

## Initialize the database
```
airflow initdb
```
## Start the web server, default port is 8080
```
airflow webserver -p 8080
```
#start the scheduler

```
airflow scheduler
```
## Visit localhost:8080 in the browser and enable the example dag in the home page

Upon running these commands, Airflow will create the $AIRFLOW_HOME folder and lay an “airflow.cfg” file with defaults that get you going fast. You can inspect the file either in $AIRFLOW_HOME/airflow.cfg, or through the UI in the Admin->Configuration menu. The PID file for the webserver will be stored in $AIRFLOW_HOME/airflow-webserver.pid or in /run/airflow/webserver.pid if started by systemd.

Out of the box, Airflow uses a sqlite database, which you should outgrow fairly quickly since no parallelization is possible using this database backend. It works in conjunction with the airflow.executors.sequential_executor.SequentialExecutor which will only run task instances sequentially. While this is very limiting, it allows you to get up and running quickly and take a tour of the UI and the command line utilities.

## Google cloud platform
It is used for uploading data from local to google cloud platform via bigquery table.
--For that First you need to create your own project and save the credential
--Afer that create dataset and the table with require feild

## Files
The below mentioned file has the functionalities and the dag
```
covid_dag.py 
```

## Run
```covid_dag.py```
Save that covid_dag.py to airflow/dag folder and then run localhost:8080.

## Dependencies
**Google cloud platform Bigquery**

pip install --upgrade google-cloud-bigquery

**Apache airflow**

pip install apache-airflow

## How airflow looks
https://docs.google.com/document/d/1Iscz60a6Xa8mnI5Mpk5Kw4cawvmfMWdmUvUY68pt5tk/edit?usp=sharing
