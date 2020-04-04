/*
QUERY 2
Per un libro, la partita iva del fornitore che lo vende al prezzo più basso e il suddetto prezzo.
*/
SELECT fornitore AS "Fornitore", prezzo AS "Prezzo"
FROM catalogo
WHERE prezzo IN (
    SELECT MIN(prezzo)
    FROM catalogo
    WHERE libro = 'X'
);

/* OPPURE */
CREATE VIEW migliori_prezzi AS (
    SELECT libro, MIN(prezzo) AS prezzo_min
    FROM catalogo
    GROUP BY libro
);

SELECT fornitore AS "Partita IVA", prezzo AS "Prezzo"
FROM catalogo
WHERE Prezzo IN (SELECT prezzo_min FROM migliori_prezzi WHERE libro = 'X');