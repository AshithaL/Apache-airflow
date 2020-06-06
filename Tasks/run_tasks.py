import covid_data as cd
from covid_dag import dag
from airflow.operators.python_operator import PythonOperator

t1 = PythonOperator(task_id="fetch_data", python_callable=cd.fetch_covid_data, dag=dag)

t2 = PythonOperator(task_id="load_data", python_callable=cd.load_data, dag=dag)

t3 = PythonOperator(task_id="percentage", python_callable=cd.read_the_data, provide_context=True, dag=dag)

t1 >> t2 >> t3