/*
Query 8: lista dei generi dei libri che appartengono ad una certa collana
*/
SELECT DISTINCT genere AS "Genere"
FROM libro JOIN appartiene
ON libro.isbn = appartiene.libro
WHERE nome_collana = XXXX;
