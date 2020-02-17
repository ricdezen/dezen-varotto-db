CREATE TABLE richiesta (
	Fornitore partita_iva NOT NULL,
	Libro isbn_code NOT NULL,
	Prenotazione INTEGER,
	Quantità smallint,
	PRIMARY KEY(Prenotazione,Libro,Fornitore),
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN),
	FOREIGN KEY Prenotazione REFERENCES prenotazione(Numero)
);
