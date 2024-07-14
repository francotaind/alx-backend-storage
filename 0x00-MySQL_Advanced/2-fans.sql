--Ranks country origin of bands, ordered by number 0f (non-unique) fans in
--descending order
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
