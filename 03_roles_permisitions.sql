CREATE ROLE webshop_reader LOGIN PASSWORD 'ChangeMe123!';

GRANT CONNECT ON DATABASE webshop TO webshop_reader;
GRANT USAGE ON SCHEMA public TO webshop_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO webshop_reader;

