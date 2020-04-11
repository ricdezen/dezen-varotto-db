/*
QUERY 5
Ottenere il bilancio economico di un certo anno, inteso come il totale vendite di libri,
meno i costi di approvvigionamento di libri, meno gli stipendi degli impiegati.
*/
SELECT
(SELECT SUM(importo) FROM acquisto) -
(SELECT SUM(importo) FROM ordine) -
(SELECT SUM(stipendio) FROM dipendente)
AS "Bilancio";
