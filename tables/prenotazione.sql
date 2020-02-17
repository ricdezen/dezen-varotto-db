CREATE TABLE prenotazione (
	Numero INTEGER,
	Dataprenotazione DATE NOT NULL,
	Prezzo smallint NOT NULL,
	Stato stato_prenotazione NOT NULL,
	Cliente fiscal_code NOT NULL,
	Dipendente fiscal_code NOT NULL,
	PRIMARY KEY(Numero),
	FOREIGN KEY Cliente REFERENCES cliente(CF),
	FOREIGN KEY Dipendente REFERENCES cliente(CF)
);
