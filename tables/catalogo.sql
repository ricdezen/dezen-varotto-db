CREATE TABLE catalogo (
	Fornitore partita_iva NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	PRIMARY KEY(Fornitore,Catalogo),
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
