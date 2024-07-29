# Use a multi-stage build
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
# RUN if [ ! -f "$LOCAL_FILE" ]; then \
#         cp /llama-2-7b-chat.Q2_K.gguf "$LOCAL_FILE"; \
#         cp /llama-2-7b-chat.Q2_K.gguf "$DOCKERFILE_DIR/models/" \
#     fi

# FROM python:3.11.1-slim
FROM python:3.10.13-slim-bullseye

# Update package lists and install Clang
RUN apt-get update && \
    apt-get install -y clang wget

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the file from the downloader stage

WORKDIR /models
COPY --from=downloader /llama-2-7b-chat.Q2_K.gguf /models/
# RUN wget -O llama-2-7b-chat.Q2_K.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf

# Install necessary system dependencies
# To install ReportLab which requires compilation, you need build-essential rather than clang
# Added 'gcc' and 'libjpeg-dev' which might be needed for ReportLab and other dependencies
RUN apt-get update && apt-get install -y \
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

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
