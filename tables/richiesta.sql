CREATE TABLE richiesta (
	Fornitore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	Prenotazione VARCHAR(20),
	Quantità smallint,
	PRIMARY KEY(Prenotazione,Libro,Fornitore),
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN),
	FOREIGN KEY Prenotazione REFERENCES prenotazione(Numero)
);
