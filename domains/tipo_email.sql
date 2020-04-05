CREATE DOMAIN tipo_email AS TEXT
CHECK (VALUE SIMILAR TO '[A-Za-z0-9.]{1,}@[A-Za-z0-9.]{1,}');