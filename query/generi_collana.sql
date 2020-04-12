SELECT DISTINCT genere AS "Genere"
FROM libro JOIN appartiene
ON libro.isbn = appartiene.libro
WHERE nome_collana = coll;
