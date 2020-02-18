CREATE TABLE libro
(
    isbn isbn_code NOT NULL,
    titolo character varying(50) NOT NULL,
    prezzo smallint NOT NULL,
    disponibili smallint NOT NULL,
    nome_collana character varying(50),
    CONSTRAINT libro_pkey PRIMARY KEY (isbn),
    CONSTRAINT libro_nome_collana_fkey FOREIGN KEY (nome_collana)
        REFERENCES collana (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
