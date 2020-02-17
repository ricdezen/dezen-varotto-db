CREATE TABLE collana (
	Nome VARCHAR(20) NOT NULL,
	Editore VARCHAR(20) NOT NULL,
	Descrizione VARCHAR(500),
	PRIMARY KEY(Nome),
	FOREIGN KEY Editore REFERENCES editore(Nome)
);
