FROM apache/airflow:latest

USER airflow
# install mlflow and psycopg2 for backend store access
RUN pip install --no-cache-dir mlflow psycopg2-binary

USER root
# add our start script
COPY start_orchestrator.sh /opt/orchestrator/start_orchestrator.sh
COPY db_init.py /opt/orchestrator/db_init.py
RUN chmod +x /opt/orchestrator/start_orchestrator.sh

# copy dags mount happens from compose; keep default airflow user
USER airflow
