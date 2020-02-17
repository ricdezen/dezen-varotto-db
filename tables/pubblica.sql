CREATE TABLE pubblica (
	Editore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	Datapubblicazione DATE,
	PRIMARY KEY(Editore,Libro),
	FOREIGN KEY Editore REFERENCES editore(Nome),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
