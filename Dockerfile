FROM python:3.9

#EXPOSE 8000

#apk update
ENV PYTHONUNBUFFERED 0
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /code/
COPY . /code/
COPY ./.env /code/
COPY ./.env_db /code/
WORKDIR /code

RUN python -m pip install --upgrade pip

RUN pip install -r ./requirements.txt

#RUN python ./restChallenge/manage.py runserver 0.0.0.0:8000
