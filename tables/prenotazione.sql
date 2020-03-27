CREATE TABLE prenotazione
(
    numero SERIAL,
    stato stato_prenotazione NOT NULL,
    data_ritiro date,
    CONSTRAINT prenotazione_pkey PRIMARY KEY (numero),
    CONSTRAINT prenotazione_data_se_chiusa CHECK (stato != 'Ritirato' OR data_ritiro IS NOT NULL)
);
