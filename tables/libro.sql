CREATE TABLE libro (
	ISBN CHAR(13) NOT NULL,
	Titolo VARCHAR(50) NOT NULL,
	Prezzo smallint,
	Disponibili smallint,
	Collana VARCHAR(20),
	PRIMARY KEY(ISBN),
	FOREIGN KEY Collana REFERENCES collana(Nome)
);
