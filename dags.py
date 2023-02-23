from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.dummy import DummyOperator

with DAG(dag_id = "dags", start_date = datetime(2022,5,1), schedule_interval = timedelta(days=1)) as dag:
    
    task1 = DummyOperator(
        task_id="task1"
    )
