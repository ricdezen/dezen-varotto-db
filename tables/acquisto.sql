CREATE TABLE acquisto(
	Numero VARCHAR(20),
	Dataacquisto DATE NOT NULL,
	Dipendente fiscal_code NOT NULL,
	Cliente fiscal_code NOT NULL,
	FOREIGN KEY Dipendente REFERENCES dipendente(CF),
	FOREIGN KEY Cliente REFERENCES Cliente(CF),
	PRIMARY KEY(Numero)
);
