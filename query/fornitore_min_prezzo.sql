SELECT distributore AS "Distributore", prezzo AS "Prezzo"
FROM catalogo
WHERE libro = XXXX
AND prezzo IN (
    SELECT MIN(prezzo)
    FROM catalogo
    WHERE libro = XXXX
);