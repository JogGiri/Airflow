from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

# scheduler_interval = None for external Trigger 
# we can use cron jobs and like @daily for schedulde interval
# cron jobs with time and timedelta with interval time

# catchup & backfilling

with DAG(dag_id='simple_dag',start_date = datetime(2022, 1, 1), schedule_interval=timedelta(days=1)) as dag:
    task1= DummyOperator(

        task_id="task-1"

    )