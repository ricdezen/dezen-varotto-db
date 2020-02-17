CREATE TABLE catalogo (
	Fornitore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	PRIMARY KEY(Fornitore,Catalogo),
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
