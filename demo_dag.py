from airflow import DAG
from airflow.models.baseoperator import chain # A function that sets sequential dependencies between tasks including lists of tasks.
#import dag and config

from datetime import datetime,timedelta

from airflow.operators.dummy import DummyOperator

#in dag file dag_id,start_date, schedule_interval
#dag run will start on startdate + interval
#default arguments

#operator which perfoerm operation
#task= operatior intialize

with DAG(dag_id="demo_dag", start_date=datetime(2022,5,13), schedule_interval=timedelta(days=1)) as dag:
    task_1=DummyOperator(
        task_id="task_1"
    )

    task_2=DummyOperator(
        task_id="task_2"
    )

    task_3=DummyOperator(
        task_id="task_3"
    )

    task_4=DummyOperator(
        task_id="task_4"
    )


    task_5=DummyOperator(
        task_id="task_5"
    )

####[task_1 ,task_2] >> [task_3] list to list will be error

#[task_1 ,task_2] >> task_3

#task_1 >> [task_2,task_3] >> task_4

chain(task_1,[task_2,task_3],[task_4,task_5])




