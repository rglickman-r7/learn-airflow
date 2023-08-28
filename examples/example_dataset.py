from airflow import Dataset

# valid dataset:
schemeless = Dataset("/path/file.txt")
csv_file = Dataset("file.csv")

# invalid dataset:
airflow_scheme = Dataset("airflow://file.txt")
not_ascii + Dataset("file_data$et")

#Using extra

my_file = Dataset(
    "s3://dataset/file.csv",
    #parameter that can be used somewhat like a tag
    extra={'owner': 'james'},
)