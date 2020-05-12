DROP DATABASE IF EXISTS agenda_db;

CREATE DATABASE IF NOT EXISTS agenda_db;
USE agenda_db;

#Create table cp
CREATE TABLE IF NOT EXISTS cps(
	cp VARCHAR(6) NOT NULL PRIMARY KEY,
	estado VARCHAR(25) NOT NULL,
    ciudad VARCHAR(25) NOT NULL
) ENGINE = InnoDB;

#Create table contactos
CREATE TABLE IF NOT EXISTS contact(
	id_contacto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(16) NOT NULL,
    a_paterno VARCHAR(16) NOT NULL,
    a_materno VARCHAR(16),
    correo VARCHAR(20),
    calle VARCHAR(20),
    numero VARCHAR(3),
    colonia VARCHAR(20),
    telefono VARCHAR(15) NOT NULL
) ENGINE = InnoDB;

#Create table citas
CREATE TABLE IF NOT EXISTS appointment(
	id_cita INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    hora VARCHAR(12) NOT NULL,
    asunto VARCHAR(40) NOT NULL,
    id_contacto INT,
    CONSTRAINT fkid_contacto FOREIGN KEY(id_contacto)
		REFERENCES contact(id_contacto)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE = InnoDB;