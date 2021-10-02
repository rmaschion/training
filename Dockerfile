FROM python:3.9
# MAINTAINER python_student

RUN FLASK_APP=flask_app/src/backend/app.py

RUN mkdir training/
COPY requirements.txt training/
COPY setup.py training/setup.py
RUN cd training_project

RUN pip3 install --upgrade pip
RUN pip3 install -e .
RUN pip3 install -r training/requirements.txt

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
