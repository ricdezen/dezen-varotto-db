/*
QUERY 6
Il codice ISBN, titolo e nome della collana di appartenenza di tutti i libri che appartengono a un certo genere.
*/
SELECT DISTINCT L.isbn AS "ISBN", L.titolo AS "Titolo", L.nome_collana AS "Collana"
FROM appartiene AS A
JOIN libro AS L
ON A.libro = L.isbn
WHERE A.genere = 'X';
