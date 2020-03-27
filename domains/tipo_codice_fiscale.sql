CREATE DOMAIN tipo_codice_fiscale AS CHAR(16)
CHECK (VALUE LIKE '[A-z|0-9]{15}');
