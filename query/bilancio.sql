SELECT
(SELECT SUM(importo) FROM acquisto WHERE date_part('year', data_acquisto) = XXXX) -
(SELECT SUM(importo) FROM ordine WHERE date_part('year', data_ordine) = XXXX) -
(SELECT SUM(stipendio) FROM dipendente)
AS "Bilancio";
