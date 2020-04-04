/*
QUERY 6
Il codice ISBN e quantità dei libri prenotati che ancora non sono stati accantonati, e il numero cliente di chi li ha ordinati.
*/
SELECT C.libro AS "Libro", C.quantita AS "Quantità", A.cliente AS "Cliente"
FROM acquisto AS A
JOIN prenotazione AS P
ON A.prenotazione = P.numero
JOIN comprende AS C
ON A.numero = C.acquisto
WHERE A.prenotazione IS NOT NULL
AND P.stato = 'Transito';