CREATE DOMAIN tipo_codice_isbn AS CHAR(13)
CHECK (VALUE LIKE '[0-9]{15}');
