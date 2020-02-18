CREATE TABLE fornitore
(
    piva partita_iva NOT NULL,
    nome character varying(50) NOT NULL,
    indirizzo character varying(50) NOT NULL,
    CONSTRAINT fornitore_pkey PRIMARY KEY (piva)
)
