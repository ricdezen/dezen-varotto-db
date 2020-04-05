CREATE DOMAIN tipo_numero_telefono AS character varying(15)
CHECK (VALUE SIMILAR TO '[0-9]{3,15}');