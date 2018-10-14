# noteapp
Application for taking  notes
This is a simple style web application for taking quick notes that needs extra attention.

http://noteapp.serverafrica.org

sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install build-essential mysql-client mysql-server python-dev virtualenv libmysqlclient-dev -y

git clone https://github.com/imosudi/noteapp.git


sudo mysqld_safe --skip-grant-tables& 
sudo mysql --user=root mysql 
#
##WAIT FOR THE MYSQL PROMPT 
#

mysql> 
update user set authentication_string=PASSWORD(''DESIRED-ROOT-password') where user='root';

flush privileges; 

quit;

sudo service mysql restart

sudo mysql -u root -p

CREATE DATABASE c6noteapp;

CREATE USER 'c6noteapp'@'%' IDENTIFIED BY  'PASSWimosudi@gmail.co767868FFGFFDD#m';
GRANT ALL PRIVILEGES ON c6noteapp.* TO 'c6noteapp'@'localhost' IDENTIFIED BY 'PASSWimosudi@gmail.co767868FFGFFDD#m';
FLUSH PRIVILEGES;

CREATE TABLE c6noteapp.users ( id INT(50) NOT NULL AUTO_INCREMENT , email VARCHAR(150) NULL DEFAULT NULL , name VARCHAR(150) NULL DEFAULT NULL , username VARCHAR(150) NULL DEFAULT NULL , password VARCHAR(150) NULL DEFAULT NULL , INDEX (id)) ENGINE = InnoDB;

CREATE TABLE c6noteapp.notes ( id INT(50) NOT NULL AUTO_INCREMENT , title VARCHAR(100) NULL DEFAULT NULL , body VARCHAR(450) NULL DEFAULT NULL , username VARCHAR(150) NULL DEFAULT NULL , INDEX (id)) ENGINE = InnoDB;

FLUSH PRIVILEGES;

quit;


cd noteapp

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python cgi-bin/noteapp/noteapp.py

