FROM python:3

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

# Netcat is a computer networking utility for reading from and writing to network 
# connections using TCP or UDP. Netcat is designed to be a dependable back-end that 
# can be used directly or easily driven by other programs and scripts.
RUN apt-get update && apt-get install -y netcat

# create an app user in the appgroup
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

# set environment variable
ENV APP_HOME=/home/app/web

RUN mkdir -p $APP_HOME/staticfiles

# set the following dir as working dir
WORKDIR $APP_HOME

# RUN mkdir /code
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . $APP_HOME

# setting permissions
RUN chown -R app:app $APP_HOME

USER app:app

# run this script after the creating of the container
ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]