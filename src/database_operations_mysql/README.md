###  Install MySQL Server
    sudo apt update
    sudo apt install mysql-server

###  Basic Setup

##### Open up the MySQL Prompt, can try commands
    sudo mysql or  mysql -u root -p
    create DATABASE Employee
     use Employee
     create TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
### To Delete DB
    drop DATABASE Employee
### Exit MySQL prompt   
    exit
### Install MySQL Connector for Python
    pip install mysql-connector-python


