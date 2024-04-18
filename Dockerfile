# Base image z docker hubu ktory bezi na debiane
# https://hub.docker.com/_/python/tags?page=&page_size=&ordering=&name=3.10.12-slim-buster
FROM python:3.10.12-slim-buster

# aby python nepisal bytovy kod a vytvra subory .pyc
ENV PYTHONDONTWRITEBYTECODE=1   
# nechceme python s vyrovnavacou pamatou
ENV PYTHONUNBUFFERED=1

# create directory for the app user 
# je to pracovny adresar vo vnutri kontajnera
# nas pocitac je vnimany ako hostitelsky a pritom
# my vytvarame linuxovy kontajner kde bude nasa aplikacia
# ktoru kontajner spusti a sem bude kontajner odkazovat
RUN mkdir -p /home/app

# don't run as root therefore create non-root user
RUN groupadd --gid 1001 app && \
    useradd --uid 1001 --gid app --home /home/app app

# install pipenv nainstaluje vsetky baliky ktore vidiet cey $ pip list
RUN pip install pipenv

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/website
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# installing dependencies - nakopirovanie nasich zavislosti
COPY Pipfile Pipfile.lock $APP_HOME # je to vlstne /home/app vytvorene vyssie

# install dependencies tu sa nainstaluje systemove baliky
# aby sme predisli konfliktom napr. pri bodkovej konvencii
RUN pipenv install --system

# copy project files and directories nakopirovanie aktualneho
# priecinku do lokality kde je vytvoreny strom webu 
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# DOCKER COMPOUSE
# Nasleduje vytvorenie Docker compose ktory spravuje pouzivnie inych kontjnerov
# v ktorych sa nachadzaju pouzivane imidze ako napr. python alebo PostgreSQL
# Pouzivaju sa n ato subory .yml ktore hovoria Dockerovi co ma s kontajnermi robit,
# ktore sluzby sa budu spustat.