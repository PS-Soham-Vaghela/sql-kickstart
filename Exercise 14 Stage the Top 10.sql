--Create the temp table
CREATE TEMP TABLE top_10_films AS
SELECT
    f.title,
    COUNT(r.rental_id) AS rentals
FROM film AS f
INNER JOIN inventory AS i
    ON f.film_id = i.film_id
INNER JOIN rental AS r
    ON i.inventory_id = r.inventory_id
GROUP BY
    f.title
ORDER BY
    rentals DESC
LIMIT 10;

--Query the temp table
SELECT
    title,
    rentals
FROM top_10_films
ORDER BY rentals DESC;
