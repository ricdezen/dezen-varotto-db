CREATE TABLE cliente
(
    cf tipo_codice_fiscale NOT NULL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    data_nascita date NOT NULL,
    telefono tipo_numero_telefono,
    email tipo_email,
    CONSTRAINT cliente_pkey PRIMARY KEY (cf),
    CONSTRAINT informazione_di_contatto CHECK (telefono IS NOT NULL OR email IS NOT NULL)
);
