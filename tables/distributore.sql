CREATE TABLE distributore
(
    piva tipo_partita_iva NOT NULL,
    nome character varying(50) NOT NULL,
    indirizzo character varying(50) NOT NULL,
    CONSTRAINT distributore_pkey PRIMARY KEY (piva)
);
