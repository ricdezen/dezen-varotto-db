SELECT DISTINCT L.isbn AS "ISBN", L.titolo AS "Titolo", L.nome_collana AS "Collana"
FROM appartiene AS A
JOIN libro AS L
ON A.libro = L.isbn
WHERE A.genere = XXXX;
