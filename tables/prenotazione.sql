CREATE TABLE prenotazione (
	Numero VARCHAR(20),
	Dataprenotazione DATE NOT NULL,
	Prezzo smallint,
	Stato VARCHAR(20),
	Cliente fiscal_code NOT NULL,
	Dipendente fiscal_code NOT NULL,
	PRIMARY KEY(Numero),
	FOREIGN KEY Cliente REFERENCES cliente(CF),
	FOREIGN KEY Dipendente REFERENCES cliente(CF)
);
