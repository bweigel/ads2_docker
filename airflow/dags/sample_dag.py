from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from app1.analysis import *

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 4, 27, 5, 30),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('sample_emr_analysis_3', default_args=default_args,
          schedule_interval='0/1 * * * *')


start_emr = PythonOperator(task_id="start_emr_and_wait_ready", python_callable=start_emr, dag=dag)
analysis = PythonOperator(task_id="run_analysis", python_callable=do_analysis, dag=dag)
load_redshift = PythonOperator(task_id="oad_to_redshift", python_callable=load_to_redshift, dag=dag)

start_emr >> analysis >> load_redshift
