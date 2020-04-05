CREATE TABLE dipendente
(
    cf tipo_codice_fiscale NOT NULL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    stipendio numeric(11,2) NOT NULL,
    CONSTRAINT dipendente_pkey PRIMARY KEY (cf),
    CONSTRAINT stipendio_positivo CHECK (stipendio > 0)
);
