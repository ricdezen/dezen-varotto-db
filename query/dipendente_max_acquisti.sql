CREATE VIEW acquisti_per_dipendente AS (
    SELECT dipendente, COUNT(*) AS acquisti
    FROM acquisto
    GROUP BY dipendente
);

SELECT A.dipendente AS "Codice Fiscale", D.nome AS "Nome", D.cognome AS "Cognome"
FROM acquisti_per_dipendente AS A
JOIN dipendente AS D
ON A.dipendente = D.cf
WHERE acquisti IN (SELECT MAX(acquisti) FROM acquisti_per_dipendente);
