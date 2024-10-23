FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./models/regression.joblib /code/models/regression.joblib
COPY ./models/music_knn.joblib /code/models/music_knn.joblib
COPY ./data/song_list.csv /code/data/song_list.csv
COPY ./app.py /code/app.py

CMD ["fastapi", "run", "app.py", "--port", "80"]