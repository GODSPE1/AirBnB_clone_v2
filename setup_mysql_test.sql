-- prepares a MySQL server for the Airbnb project

-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- create a new user and grant permisions
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
