/*
QUERY 2
Per un libro, la partita iva del fornitore che lo vende al prezzo più basso e il suddetto prezzo.
*/
SELECT distributore AS "Distributore", prezzo AS "Prezzo"
FROM catalogo
WHERE libro = XXXX
AND prezzo IN (
    SELECT MIN(prezzo)
    FROM catalogo
    WHERE libro = XXXX
);