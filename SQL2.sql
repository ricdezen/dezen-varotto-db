# De Zen & Varotto's Database course project
CREATE TABLE cliente
(
	CF VARCHAR(20),
	Nome VARCHAR(20) NOT NULL,
	Cognome VARCHAR(20) NOT NULL,
	Datadinascita DATE NOT NULL,
	PRIMARY KEY(CF)
);

CREATE TABLE dipendente
(
	CF VARCHAR(20),
	Nome VARCHAR(20) NOT NULL,
	Cognome VARCHAR(20) NOT NULL,
	Stipendio int NOT NULL,
	PRIMARY KEY(CF)
);

CREATE TABLE acquisto
(
	Numero VARCHAR(20),
	Data DATE NOT NULL,
	Dipendente VARCHAR(20) NOT NULL,
	Cliente VARCHAR(20) NOT NULL,
	FOREIGN KEY Dipendente REFERENCES dipendente(CF),
	FOREIGN KEY Cliente REFERENCES Cliente(CF),
	PRIMARY KEY(Numero)
);

CREATE TABLE include 
(
	Libro VARCHAR(20) NOT NULL,
	Acquisto VARCHAR(20),
	Quantità int,
	FOREIGN KEY Acquisto REFERNCES acquisto(Numero),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);

CREATE TABLE autore
(	
	ID VARCHAR(20),
	Nome VARCHAR(20) NOT NULL,
	Cognome VARCHAR(20) NOT NULL,
	Datadinascita DATE NOT NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE scrive 
(
	Autore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	FOREIGN KEY Autore REFERNCES autore(ID),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);

CREATE TABLE libro 
(
	ISBN CHAR(13) NOT NULL,
	Titolo VARCHAR(50) NOT NULL,
	Prezzo smallint,
	Disponibili smallint,
	Collana VARCHAR(20),
	PRIMARY KEY(ISBN),
	FOREIGN KEY Collana REFERENCES collana(Nome)
);

CREATE TABLE pubblica
(	
	Editore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	Data DATE,
	FOREIGN KEY Editore REFERENCES editore(Nome),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);

CREATE TABLE editore
(
	Nome VARCHAR(20) NOT NULL,
	PRIMARY KEY(Nome)
);

CREATE TABLE collana
(
	Nome VARCHAR(20) NOT NULL,
	Editore VARCHAR(20) NOT NULL,
	Descrizione VARCHAR(500),
	PRIMARY KEY(Nome),
	FOREIGN KEY Editore REFERENCES editore(Nome)
);

CREATE TABLE appartiene 
(	
	Genere VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	FOREIGN KEY Libro REFERENCES libro(ISBN),
	FOREIGN KEY Genere REFERENCES genere(Nome)
);

CREATE TABLE genere
(
	Nome VARCHAR(20) NOT NULL,
	Descrizione VARCHAR(500),
	PRIMARY KEY(Nome)
);

CREATE TABLE fornitore
(	PIVA VARCHAR(20) NOT NULL,
	Nome VARCHAR(20) NOT NULL,
	Indirizzo VARCHAR(20) NOT NULL,
	PRIMARY KEY(PIVA)
);

CREATE TABLE catalogo
(
	Fornitore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);

CREATE TABLE richiesta
(
	Fornitore VARCHAR(20) NOT NULL,
	Libro VARCHAR(20) NOT NULL,
	Prenotazione VARCHAR(20),
	Quantità smallint,
	FOREIGN KEY Fornitore REFERENCES fornitore(PIVA),
	FOREIGN KEY Libro REFERENCES libro(ISBN),
	FOREIGN KEY Prenotazione REFERENCES prenotazione(Numero)
);

CREATE TABLE prenotazione
(
	Numero VARCHAR(20),
	Data DATE NOT NULL,
	Prezzo smallint,
	Stato VARCHAR(20),
	Cliente VARCHAR(20) NOT NULL,
	Dipendente VARCHAR(20) NOT NULL,
	PRIMARY KEY(Numero),
	FOREIGN KEY Cliente REFERENCES cliente(CF),
	FOREIGN KEY Dipendente REFERENCES cliente(CF)
);
	
	
	
