CREATE TABLE prenotazione
(
    numero integer NOT NULL,
    stato stato_prenotazione NOT NULL,
    cliente integer NOT NULL,
    data_ritiro date,
    CONSTRAINT prenotazione_pkey PRIMARY KEY (numero),
    CONSTRAINT prenotazione_fkey_acquisto FOREIGN KEY (numero)
        REFERENCES acquisto (numero) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT prenotazione_fkey_cliente FOREIGN KEY (cliente)
        REFERENCES cliente (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT prenotazione_data_se_chiusa CHECK (stato != 'Ritirato' OR data_ritiro IS NOT NULL)
);
