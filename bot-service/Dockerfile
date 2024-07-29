FROM alpine AS downloader

# Check if the file exists on the host machine
ARG LOCAL_FILE=./models/llama-2-7b-chat.Q2_K.gguf
RUN if [ -f "$LOCAL_FILE" ]; then \
        cp "$LOCAL_FILE" /llama-2-7b-chat.Q2_K.gguf; \
    else \
        wget -O /llama-2-7b-chat.Q2_K.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf; \
    fi

# Check if the local file exists, if not, copy it from the container to the host
ARG DOCKERFILE_DIR

FROM python:3.10.13-slim-bullseye

# Update package lists and install Clang
RUN apt-get update && \
    apt-get install -y clang wget

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the file from the downloader stage

WORKDIR /models
COPY --from=downloader /llama-2-7b-chat.Q2_K.gguf /models/

WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
