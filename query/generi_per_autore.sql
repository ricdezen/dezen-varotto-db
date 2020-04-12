/*
Query 7: Lista dei generi scritti da un'autore
*/
SELECT DISTINCT genere AS "Genere"
FROM scrive NATURAL JOIN appartiene
WHERE autore = XXXX;
