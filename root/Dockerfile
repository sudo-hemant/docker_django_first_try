FROM python:3

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apt-get update && apt-get install -y netcat

# create an app user in the appgroup
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

ENV APP_HOME=/home/app/web

RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

# RUN mkdir /code
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app:app

ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]