CREATE TABLE prenotazione
(
    numero SERIAL,
    dataprenotazione date NOT NULL,
    prezzo smallint NOT NULL,
    stato stato_prenotazione NOT NULL,
    nome_cliente fiscal_code NOT NULL,
    nome_dipendente fiscal_code NOT NULL,
    CONSTRAINT prenotazione_pkey PRIMARY KEY (numero),
    CONSTRAINT prenotazione_nome_cliente_fkey FOREIGN KEY (nome_cliente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT prenotazione_nome_dipendente_fkey FOREIGN KEY (nome_dipendente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
