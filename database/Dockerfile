# Use the official PostgreSQL image as the base image
FROM postgres:latest

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=silastech

# Copy DDL scripts and sample data into the container
COPY /seed/* /docker-entrypoint-initdb.d/

# Expose PostgreSQL default port
EXPOSE 5432