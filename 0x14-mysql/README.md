# ALX 2023 Software Engineering - MySQL

<!-- TASK 00 -->
 sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57

<!-- TASK 01  -->
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

<!-- TASK 02 -->
CREATE DATABASE tyrell_corp;
CREATE TABLE nexus6 ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, description TEXT);
INSERT INTO nexus6 (name, description) VALUES ('Google Nexus 7', 'A popu
lar Android tablet.');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

<!-- TASK 03 -->
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

sudo ufw allow from 54.145.156.135 to any port 3306


CHANGE REPLICATION SOURCE TO SOURCE_HOST='3.86.18.143',SOURCE_USER='holberton_user',SOURCE_PASSWORD='projectcorrection280hbtn',
SOURCE_LOG_FILE='mysql-bin.000001',
SOURCE_LOG_POS=899;


GRANT REPLICATION SLAVE ON *.* TO 'holberton_user'@'54.145.156.135';
