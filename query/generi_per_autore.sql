/*
Query 8: Lista dei generi scritti da un'autore
*/
SELECT genere AS "Genere"
FROM scrive NATURAL JOIN appartiene
WHERE autore = 'X';
