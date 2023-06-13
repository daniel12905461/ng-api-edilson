DROP DATABASE IF EXISTS proyecto_edilson;
CREATE DATABASE proyecto_edilson;
USE proyecto_edilson;

CREATE TABLE rols(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL
);

CREATE TABLE socios(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombres VARCHAR(45) NOT NULL,
  apellidos VARCHAR(45) NOT NULL,
  ci VARCHAR(45) NOT NULL,
  foto VARCHAR(45) NOT NULL,
  celular VARCHAR(45) NULL,
  fecha_nac DATE NOT NULL,
  user VARCHAR(45) NULL,
  password VARCHAR(45) NULL,
  id_rols INT NOT NULL,
  FOREIGN KEY (id_rols) REFERENCES rols(id)
);
