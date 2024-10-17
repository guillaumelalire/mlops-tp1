FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./regression.joblib /code/regression.joblib
COPY ./app.py /code/app.py

CMD ["fastapi", "run", "app.py", "--port", "80"]