# Producing data by updating a dataset 

from airflow import DAG, Dataset
# allows us to create task operators in a quicker way
from airflow.decorators import task

from datetime import datetime

# Defining the URI or path to the dataset
my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False
):
    

    # outlet parameter defines what dataset we want to update
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("producer update")

    update_dataset()

    # outlet parameter defines what dataset we want to update
    @task(outlets=[my_file_2])
    def update_dataset_2():
        with open(my_file_2.uri, "a+") as f:
            f.write("producer update")

    update_dataset_2()