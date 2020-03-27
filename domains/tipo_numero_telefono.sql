CREATE DOMAIN tipo_codice_isbn AS character varying(15)
CHECK (VALUE LIKE '[0-9]{14}');