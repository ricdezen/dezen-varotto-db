/*
QUERY 5
Ottenere il bilancio economico di un certo anno, inteso come il totale vendite di libri,
meno i costi di approvvigionamento di libri, meno gli stipendi degli impiegati.
*/
SELECT
(SELECT SUM(importo) FROM acquisto WHERE date_part('year', data_acquisto) = XXXX) -
(SELECT SUM(importo) FROM ordine WHERE date_part('year', data_ordine) = XXXX) -
(SELECT SUM(stipendio) FROM dipendente)
AS "Bilancio";
