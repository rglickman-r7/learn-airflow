try:
    import airflow
    print("Apache Airflow is installed.")
except ImportError:
    print("Apache Airflow is not installed.")