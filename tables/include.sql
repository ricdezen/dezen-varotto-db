CREATE TABLE include (
	Libro isbn_code NOT NULL,
	Acquisto INTEGER NOT NULL,
	Quantità INTEGER NOT NULL,
	PRIMARY KEY(Libro,Acquisto),
	FOREIGN KEY Acquisto REFERNCES acquisto(Numero),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
