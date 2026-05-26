CREATE DATABASE votaciones;

CREATE TABLE candidatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    candidato_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (candidato_id)
    REFERENCES candidatos(id)
);

-- select * from candidatos;
-- select * from votos;

INSERT INTO candidatos (nombre)
VALUES ("Nexo");

INSERT INTO candidatos (nombre)
VALUES ("Volt");

INSERT INTO candidatos (nombre)
VALUES ("Pixel");

INSERT INTO candidatos (nombre)
VALUES ("Tekno");

INSERT INTO candidatos (nombre)
VALUES ("Sigma");

INSERT INTO candidatos (nombre)
VALUES ("Nova");