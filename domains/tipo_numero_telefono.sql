CREATE DOMAIN tipo_numero_telefono AS character varying(15)
CHECK (VALUE LIKE '[0-9]{3,14}');