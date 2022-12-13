from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
import random


def hello():
    print("Airflow")


def two_digit():
    print(random.randint(1, 100), random.randint(1, 100))


def two_digit_file():
    with open("two_digit.txt", "a") as f:
        print(random.randint(1, 100), random.randint(1, 100), file=f)


def summa():
    summa_1 = 0
    summa_2 = 0
    with open("two_digit.txt", "r") as f:
        for line in f.readlines():
            if len(line.strip().split()) == 2:
                summa_1 = summa_1 + int(line.strip().split()[0])
                summa_2 = summa_2 + int(line.strip().split()[1])
    raznost = summa_1 - summa_2
    with open("two_digit.txt", "a") as f:
        f.write(str(raznost) + "\n")


def rewrite_digit():
    with open("two_digit.txt", "r") as f:
        all_file = f.readlines()[0:-1]
    with open("two_digit.txt", "w") as f:
        f.writelines(all_file)
        f.write("\n")
        print(random.randint(1, 100), random.randint(1, 100), file=f)


with DAG(dag_id="first_dag", start_date=datetime(2022, 1, 1), schedule="* * * * *", max_active_runs=5) as dag:
    bash_task = BashOperator(task_id="hello", bash_command="echo hello")
    python_task = PythonOperator(task_id="world", python_callable=hello)
    python_task_2 = PythonOperator(
        task_id="two_digit", python_callable=two_digit)
    python_task_3 = PythonOperator(
        task_id="two_digit_file", python_callable=two_digit_file)
    python_task_4 = PythonOperator(
        task_id="two_digit_file_raznost", python_callable=summa)
    python_task_5 = PythonOperator(
        task_id="rewrite_digit", python_callable=rewrite_digit)
    bash_task >> python_task >> python_task_2 >> python_task_3 >> python_task_4 >> python_task_5
