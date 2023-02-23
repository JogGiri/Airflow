from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.dummy import DummyOperator

# dag id,start_date ,schedule_interval,default_argument
#@daily

with DAG(dag_id="rajesh", start_date=datetime(2022,11,5), schedule_interval=timedelta(days=1)) as dag:

    task_1 = DummyOperator(
        task_id="rajesh_first_dag"
    )