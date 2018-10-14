# noteapp
Application for taking  notes
This is a simple style web application for taking quick notes that needs extra attention.

http://noteapp.serverafrica.org

sudo apt-get update & sudo apt-get upgrade -y && sudo apt-get install build-essential python-dev virtualenv libmysqlclient-dev -y

git clone https://github.com/imosudi/noteapp.git

CREATE USER 'c6noteapp'@'%' IDENTIFIED WITH mysql_native_password AS 'imosudi@gmail.com';GRANT USAGE ON *.* TO 'c6noteapp'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `c6noteapp`;GRANT ALL PRIVILEGES ON `c6noteapp`.* TO 'c6noteapp'@'%';GRANT ALL PRIVILEGES ON `c6noteapp\_%`.* TO 'c6noteapp'@'%';


CREATE TABLE `c6noteapp`.`users` ( `id` INT(50) NOT NULL AUTO_INCREMENT , `email` VARCHAR(150) NULL DEFAULT NULL , `name` VARCHAR(150) NULL DEFAULT NULL , `username` VARCHAR(150) NULL DEFAULT NULL , `password` VARCHAR(150) NULL DEFAULT NULL , INDEX (`id`)) ENGINE = InnoDB;

cd noteapp

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python cgi-bin/noteapp/noteapp.py
