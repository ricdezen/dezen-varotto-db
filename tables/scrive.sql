CREATE TABLE scrive (
	Autore VARCHAR(20) NOT NULL,
	Libro isbn_code NOT NULL,
	FOREIGN KEY Autore REFERNCES autore(ID),
	FOREIGN KEY Libro REFERENCES libro(ISBN)
);
