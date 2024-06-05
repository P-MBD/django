FROM python:3.8-slim-buster
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app/
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

