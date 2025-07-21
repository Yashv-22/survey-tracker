CREATE DATABASE IF NOT EXISTS survey_db;
USE survey_db;

CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_code VARCHAR(50) NOT NULL UNIQUE,
    client_name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    cpi DECIMAL(10, 2) NOT NULL,
    loi INT NOT NULL,
    status ENUM('Live', 'Paused', 'Closed') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
