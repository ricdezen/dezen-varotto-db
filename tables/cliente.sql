CREATE TABLE cliente
(
    cf fiscal_code NOT NULL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    data_nascita date NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (cf)
)
