CREATE TABLE libro
(
    isbn codice_isbn NOT NULL,
    titolo character varying(50) NOT NULL,
    prezzo smallint NOT NULL,
    disponibili smallint NOT NULL,
    nome_collana character varying(50),
    CONSTRAINT libro_pkey PRIMARY KEY (isbn),
    CONSTRAINT libro_nome_collana_fkey FOREIGN KEY (nome_collana)
        REFERENCES collana (nome) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT prezzo_positivo CHECK (prezzo > 0),
    CONSTRAINT disponibili_non_negativo CHECK (disponibili >= 0)
)
