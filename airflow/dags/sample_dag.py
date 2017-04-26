from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from app1.get_tanker_info import write_wot_stats

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 4, 26),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('wot_stuff_2', default_args=default_args,
          schedule_interval='0 0 0/1 * * *')


task_write = PythonOperator(task_id="append_json", python_callable=write_wot_stats, dag=dag)
task_sleep = BashOperator(task_id='sleep', bash_command='sleep 5',
                          dag=dag)
task_world = BashOperator(task_id='print_world',
                          bash_command='echo "world"', retries=3,
                          dag=dag)

task_write >> task_sleep >> task_world
