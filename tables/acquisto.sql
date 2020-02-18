CREATE TABLE acquisto
(
    numero SERIAL,
    dataacquisto date NOT NULL,
    dipendente fiscal_code COLLATE NOT NULL,
    cliente fiscal_code COLLATE NOT NULL,
    CONSTRAINT acquisto_pkey PRIMARY KEY (numero),
    CONSTRAINT acquisto_cliente_fkey FOREIGN KEY (cliente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT acquisto_dipendente_fkey FOREIGN KEY (dipendente)
        REFERENCES dipendente (cf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
