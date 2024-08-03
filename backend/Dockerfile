FROM python:3.10.13-slim-bullseye

RUN apt-get update && \
    apt-get install -y clang wget && \
apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# COPY ./models/* /models/
# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
