CREATE USER 'zmuser'@'localhost' IDENTIFIED BY 'zmpass';
GRANT ALL PRIVILEGES ON `zm` . * TO 'zmuser'@'localhost';