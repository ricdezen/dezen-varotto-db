CREATE TABLE a_immediato (
    numero integer NOT NULL,
    cliente integer,
    CONSTRAINT immediato_pkey PRIMARY KEY (numero),
    CONSTRAINT immediato_fkey_acquisto FOREIGN KEY (numero)
        REFERENCES acquisto (numero) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT immediato_fkey_cliente FOREIGN KEY (cliente)
        REFERENCES cliente (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);