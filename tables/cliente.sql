CREATE TABLE cliente
(
    cf tipo_codice_fiscale NOT NULL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    data_nascita date NOT NULL,
    telefono tipo_numero_telefono NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (cf)
);
