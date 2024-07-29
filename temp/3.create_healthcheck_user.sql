CREATE ROLE healthcheck_user WITH LOGIN PASSWORD 'your_password';

CREATE USER ${HEALTHCHECK_USER} WITH PASSWORD '${HEALTHCHECK_PASSWORD}';
-- Grant connect privilege on the database
-- have db name be fed from env
-- GRANT CONNECT ON DATABASE silastech TO ${HEALTHCHECK_USER};

-- -- Allow the user to login
-- ALTER ROLE ${HEALTHCHECK_USER} WITH LOGIN;


-- -- Create the role
-- CREATE ROLE healthcheck_role;

-- -- Create the user and associate it with the role
-- CREATE USER healthcheck_user WITH PASSWORD 'your_password';
-- GRANT healthcheck_role TO healthcheck_user;

-- -- Grant the user permission to connect to the test database
-- GRANT CONNECT ON DATABASE silastech TO healthcheck_role;
