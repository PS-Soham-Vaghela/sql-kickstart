--Step 1 Create the view
CREATE VIEW film_catalog AS
SELECT
    f.title,
    c.name AS category,
    f.rental_rate,
    f.length
FROM film f
JOIN film_category fc
    ON f.film_id = fc.film_id
JOIN category c
    ON fc.category_id = c.category_id;

--Step 2 Query the view
SELECT
    title,
    rental_rate,
    length
FROM film_catalog
WHERE category = 'Comedy'
ORDER BY title;
