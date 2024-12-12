CREATE DATABASE IF NOT EXISTS price_comparator;
USE price_comparator;
 
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price VARCHAR(50) NOT NULL,
    link TEXT NOT NULL,
    image TEXT, -- Colonne pour les URLs des images
    site VARCHAR(50) NOT NULL
);