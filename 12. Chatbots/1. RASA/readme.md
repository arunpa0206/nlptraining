Step 1 : Install RASA

`pip install rasa`

Step 2: To check RASA is installed

`rasa -h`

Step 3: Initialise RASA Chatbot (if you have cloned the repository and running existing RASA code, you don't need to do this)

`rasa init`

Step 4: To start chatting with the bot

`rasa shell`

Step 5: In case you make modification in the rasa training data and code

`rasa train`
`rasa test` (optional)
`rasa shell`

Step 6: Install MySQL in Windows

Go over this link to download MySQL Installer - https://dev.mysql.com/downloads/installer/
Run the installer by keeping default settings.

Step 7: Open Commnad Prompt or Powershell or can search for MySQL Client from Windows Search bar

`mysql -u root`

Step 8: After logging into MySQL Server without password, we have to set the password

`ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';`

Step 9: Now, you will be able to use your new password to log in to MySQL server

`mysql -u root -p`

And type the password.

Step 10. Create the Database

`create database telecom`

Step 11. Use telecom Database

`use telecom`

Step 12. Create table test in telecom Database

CREATE TABLE `test` ( `id` int NOT NULL, `month_name` varchar(255) NOT NULL, `activity` varchar(255) DEFAULT NULL, PRIMARY KEY (`id`))

Step 13. Insert one value in the table.

INSERT INTO `telecom`.`test` (`id`, `month_name`, `activity`) VALUES ("1", "January", "high usage");

Step 14. Exit the MySQL server

`exit`

Step 15: To run Action Server

`rasa run actions`

