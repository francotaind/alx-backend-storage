--Create a table users with the following columns:
--id: INT, AUTO_INCREMENT, PRIMARY KEY
--email: VARCHAR(255), NOT NULL, UNIQUE
--name: VARCHAR(255)

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
