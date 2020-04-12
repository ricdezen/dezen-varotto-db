/*
QUERY 3
Il nome, la descrizione e il numero di libri venduti del genere di cui è stato venduto il maggior numero di libri.
*/
CREATE VIEW vendite_per_genere AS (
    SELECT AP.genere AS genere, SUM(CO.quantita) AS quantita 
    FROM (
        acquisto AS AQ
        JOIN comprende AS CO 
        ON AQ.numero = CO.acquisto
        JOIN appartiene AS AP
        ON AP.libro = CO.libro
    )
    GROUP BY genere
);

SELECT G.nome AS "Genere più venduto", G.descrizione AS "Descrizione", V.quantita AS "Vendite"
FROM vendite_per_genere AS V
JOIN genere AS G
ON G.nome = V.genere
WHERE V.quantita IN (
    SELECT MAX(quantita) FROM vendite_per_genere
);