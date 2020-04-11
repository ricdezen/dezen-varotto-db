/*
  Query 1
*/
CREATE FUNCTION dipendente_piu_vendite ()
RETURNS TABLE(
	"Codice Fiscale" tipo_codice_fiscale,
	"Nome" character varying(20),
	"Cognome" character varying(20)
) AS $$
    SELECT A.dipendente AS "Codice Fiscale", D.nome AS "Nome", D.cognome AS "Cognome"
	FROM acquisti_per_dipendente AS A
	JOIN dipendente AS D
	ON A.dipendente = D.cf
	WHERE acquisti IN (SELECT MAX(acquisti) FROM acquisti_per_dipendente);
$$ LANGUAGE SQL;

/*
  Query 4
*/
CREATE FUNCTION case_editrici_vendite (giorno date)
RETURNS TABLE("Casa Editrice" character varying(20)) AS $$
    SELECT DISTINCT L.nome_editore AS "Casa Editrice"
		FROM libro AS L
		JOIN comprende AS C
		ON L.isbn = C.libro
		JOIN acquisto AS A
		ON C.acquisto = A.numero
	  WHERE A.data_acquisto = giorno;
$$ LANGUAGE SQL;

/*
  Query 7
*/
CREATE FUNCTION bilancio () RETURNS numeric(11,2) AS $$
    SELECT
		(SELECT SUM(importo) FROM acquisto) -
		(SELECT SUM(importo) FROM ordine) -
		(SELECT SUM(stipendio) FROM dipendente)
	  AS "Bilancio";
$$ LANGUAGE SQL;
