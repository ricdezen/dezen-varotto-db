/*
QUERY 1
Trovare il codice fiscale, nome e cognome del Dipendente che ha registrato il maggior numero di Acquisti dei clienti.
*/
CREATE VIEW acquisti_per_dipendente AS (
    SELECT dipendente, COUNT(*) AS acquisti
    FROM acquisto
    GROUP BY dipendente
);

SELECT A.dipendente AS "Codice Fiscale", 
FROM acquisti_per_dipendente AS A
JOIN dipendente AS D
ON A.dipendente = D.cf
WHERE acquisti IN (SELECT MAX(acquisti) FROM acquisti_per_dipendente);