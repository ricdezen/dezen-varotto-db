CREATE TABLE collana
(
    nome character varying(50) NOT NULL,
    nome_editore character varying(50) NOT NULL,
    descrizione text,
    CONSTRAINT collana_pkey PRIMARY KEY (nome),
    CONSTRAINT collana_nome_editore_fkey FOREIGN KEY (nome_editore)
        REFERENCES editore (nome) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION
)
