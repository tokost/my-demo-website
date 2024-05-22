# Base image z docker hubu ktory bezi na debiane
# https://hub.docker.com/_/python/tags?page=&page_size=&ordering=&name=3.10.12-slim-buster
FROM python:3.10.12-slim-buster

# Set environment variables
# aby python nepisal bytovy kod a vytvra subory .pyc
ENV PYTHONDONTWRITEBYTECODE=1   
# nechceme python s vyrovnavacou pamatou
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /home/app/website

# Copy the project files into the container
##COPY . .
# Copy the dependencies file to the working directory
COPY requirements.txt .

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

# Install project dependencies
RUN pip install -r requirements.txt

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/website

# Install python-dotenv
RUN pip install python-dotenv

# Create necessary directories
##RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# installing dependencies - nakopirovanie nasich zavislosti
##COPY Pipfile Pipfile.lock $APP_HOME # je to vlstne /home/app vytvorene vyssie

# install dependencies tu sa nainstaluje systemove baliky
# aby sme predisli konfliktom napr. pri bodkovej konvencii
##RUN pipenv install --system

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files and directories nakopirovanie aktualneho
# priecinku do lokality kde je vytvoreny strom webu 
COPY . $APP_HOME

# Copy the requirements file into the container
COPY ./requirements.txt /tmp/requirements.txt

# Install project dependencies
RUN pip install -r /tmp/requirements.txt

# Change ownership of the working directory
RUN chown -R app:app /home/app/website


# Switch to the app user
USER app

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]