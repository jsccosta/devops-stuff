-- -- Create the database
-- CREATE DATABASE silastech;

-- Connect to the newly created database
\c silastech;

-- Create the schema
-- CREATE SCHEMA silas;
CREATE SCHEMA IF NOT EXISTS silas;

-- Create the role
CREATE ROLE health;

-- Grant necessary privileges to the role
GRANT CONNECT ON DATABASE silastech TO health;
GRANT USAGE ON SCHEMA silas TO health;

-- Create the user and associate it with the role
CREATE USER healthcheck_user WITH PASSWORD 'password';
GRANT health TO healthcheck_user;

-- Exit psql
\q