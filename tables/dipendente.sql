CREATE TABLE dipendente
(
    cf tipo_codice_fiscale NOT NULL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    stipendio integer NOT NULL,
    CONSTRAINT dipendente_pkey PRIMARY KEY (cf),
    CONSTRAINT stipendio_positivo CHECK (stipendio > 0)
);
