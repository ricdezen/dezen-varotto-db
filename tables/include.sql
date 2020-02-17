CREATE TABLE include (
	Libro VARCHAR(20) NOT NULL,
	Acquisto VARCHAR(20),
	Quantità int,
	PRIMARY KEY(Libro,Acquisto),
	FOREIGN KEY Acquisto REFERNCES acquisto(Numero),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
