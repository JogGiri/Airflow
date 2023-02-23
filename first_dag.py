from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {
    "retry": 5,
    "retry_delay": timedelta(minutes=5)
}

def _downloading_data(**kwargs):
    print("just_test")
    print(kwargs)
    #print(my_param)

with DAG(dag_id="first_dag", default_args=default_args, start_date=datetime(2022,1,1), schedule_interval="@daily", catchup=True) as dag:

    # task_1 = DummyOperator(
    #     task_id="task_1"
    #     #retry=5,
    #     #retry_delay=timedelta(minutes=5)
    #     #commentes because of default argument
    #     )

    # task_2 = DummyOperator(
    #     task_id="task_2",
    #     #retry=3 #################showwing error
    #     #retry=5
    #     #retry_delay=timedelta(minutes=5)
    #     #retry=3
    # )

    downloading_data = PythonOperator(
        task_id="downloading_data",
        python_callable= _downloading_data
        #op_kwargs={"my_param":42}
    )
