CREATE TABLE appartiene (
	Genere VARCHAR(20) NOT NULL,
	Libro isbn_code NOT NULL,
	PRIMARY KEY(Libro,Genere),
	FOREIGN KEY Libro REFERENCES libro(ISBN),
	FOREIGN KEY Genere REFERENCES genere(Nome)
);
