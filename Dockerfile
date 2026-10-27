
FROM quay.io/jupyter/scipy-notebook:latest

WORKDIR /home/jovyan/bd-a1

COPY --chown=jovyan:users requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=jovyan:users data/ ./data/
COPY --chown=jovyan:users notebook/ ./notebook/

EXPOSE 8888

CMD ["start-notebook.py", "--ServerApp.root_dir=/home/jovyan/bd-a1"]
