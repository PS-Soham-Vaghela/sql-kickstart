import psycopg2
from openpyxl import Workbook

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "dvdrental",
    "user": "Your_Postgrel_Username",
    "password": "Your_Postgrel_Password",
    "port": 5432
}

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

wb = Workbook()
wb.remove(wb.active)


# Helper Function


def export_sheet(sheet_name, sql):
    cursor.execute(sql)

    headers = [desc[0] for desc in cursor.description]

    ws = wb.create_sheet(sheet_name)

    ws.append(headers)

    for row in cursor.fetchall():
        ws.append(row)


# Q1


export_sheet(
    "Q1",
    """
    SELECT
        title AS "Film Title",
        rental_rate AS "Daily Price"
    FROM film
    ORDER BY title
    LIMIT 10;
    """
)


# Q2


export_sheet(
    "Q2",
    """
    SELECT
        title,
        length
    FROM film
    WHERE length BETWEEN 60 AND 120
      AND title LIKE 'A%'
    ORDER BY length;
    """
)


# Q3


export_sheet(
    "Q3",
    """
    SELECT
        rating,
        COUNT(*) AS film_count
    FROM film
    GROUP BY rating
    ORDER BY film_count DESC;
    """
)

# ---------------------------------------
# Q4
# ---------------------------------------

export_sheet(
    "Q4",
    """
    SELECT
        c.name AS category,
        COUNT(*) AS film_count
    FROM category c
    JOIN film_category fc
      ON c.category_id = fc.category_id
    GROUP BY c.name
    HAVING COUNT(*) > 65
    ORDER BY film_count DESC;
    """
)

# ---------------------------------------
# Q5
# ---------------------------------------

export_sheet(
    "Q5",
    """
    SELECT
        f.title,
        c.name AS category
    FROM film f
    JOIN film_category fc
      ON f.film_id = fc.film_id
    JOIN category c
      ON fc.category_id = c.category_id
    ORDER BY c.name, f.title;
    """
)

# ---------------------------------------
# Q6
# ---------------------------------------

export_sheet(
    "Q6",
    """
    SELECT
        UPPER(first_name || ' ' || last_name) AS customer_name,
        SUBSTRING(email FROM POSITION('@' IN email)+1) AS email_domain
    FROM customer;
    """
)

# ---------------------------------------
# Q7
# ---------------------------------------

export_sheet(
    "Q7",
    """
    SELECT
        first_name,
        last_name,
        'Actor' AS type
    FROM actor

    UNION ALL

    SELECT
        first_name,
        last_name,
        'Staff'
    FROM staff;
    """
)

# ---------------------------------------
# Q8
# ---------------------------------------

export_sheet(
    "Q8",
    """
    SELECT
        CASE
            WHEN length < 60 THEN 'Short'
            WHEN length BETWEEN 60 AND 120 THEN 'Medium'
            ELSE 'Long'
        END AS length_bucket,
        COUNT(*) AS films
    FROM film
    GROUP BY length_bucket
    ORDER BY films DESC;
    """
)

# ---------------------------------------
# Q9
# ---------------------------------------

export_sheet(
    "Q9",
    """
    WITH customer_spending AS (
        SELECT
            c.customer_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            SUM(p.amount) AS total_spent
        FROM customer c
        JOIN payment p
          ON c.customer_id = p.customer_id
        GROUP BY
            c.customer_id,
            c.first_name,
            c.last_name
    )

    SELECT
        customer_name,
        total_spent
    FROM customer_spending
    WHERE total_spent >
    (
        SELECT AVG(total_spent)
        FROM customer_spending
    )
    ORDER BY total_spent DESC;
    """
)

# ---------------------------------------
# Q10
# ---------------------------------------

export_sheet(
    "Q10",
    """
    SELECT
        title,
        rental_rate
    FROM film
    WHERE rental_rate >
    (
        SELECT AVG(rental_rate)
        FROM film
    )
    ORDER BY rental_rate DESC;
    """
)

# ---------------------------------------
# Q11
# ---------------------------------------

export_sheet(
    "Q11",
    """
    SELECT
        c.name AS category,
        f.title,
        COUNT(r.rental_id) AS rentals,
        RANK() OVER(
            PARTITION BY c.name
            ORDER BY COUNT(r.rental_id) DESC
        ) AS rnk
    FROM film f
    JOIN film_category fc
      ON f.film_id = fc.film_id
    JOIN category c
      ON fc.category_id = c.category_id
    JOIN inventory i
      ON f.film_id = i.film_id
    JOIN rental r
      ON i.inventory_id = r.inventory_id
    GROUP BY
        c.name,
        f.title
    ORDER BY
        c.name,
        rnk;
    """
)

# ---------------------------------------
# Q12 (View)
# ---------------------------------------

cursor.execute("DROP VIEW IF EXISTS film_catalog CASCADE;")

cursor.execute("""
CREATE VIEW film_catalog AS
SELECT
    f.title,
    c.name AS category,
    f.rental_rate,
    f.length
FROM film f
JOIN film_category fc
ON f.film_id=fc.film_id
JOIN category c
ON fc.category_id=c.category_id;
""")

export_sheet(
    "Q12",
    """
    SELECT
        title,
        rental_rate,
        length
    FROM film_catalog
    WHERE category='Comedy'
    ORDER BY title;
    """
)

# ---------------------------------------
# Q13 (Materialized View)
# ---------------------------------------

cursor.execute("DROP MATERIALIZED VIEW IF EXISTS category_revenue;")

cursor.execute("""
CREATE MATERIALIZED VIEW category_revenue AS
SELECT
    c.name AS category,
    SUM(p.amount) AS revenue
FROM payment p
JOIN rental r
ON p.rental_id=r.rental_id
JOIN inventory i
ON r.inventory_id=i.inventory_id
JOIN film_category fc
ON i.film_id=fc.film_id
JOIN category c
ON fc.category_id=c.category_id
GROUP BY c.name;
""")

export_sheet(
    "Q13",
    """
    SELECT
        category,
        revenue
    FROM category_revenue
    ORDER BY revenue DESC
    LIMIT 5;
    """
)

cursor.execute(
    "REFRESH MATERIALIZED VIEW category_revenue;"
)

# ---------------------------------------
# Q14 (Temporary Table)
# ---------------------------------------

cursor.execute("""
CREATE TEMP TABLE top_10_films AS
SELECT
    f.title,
    COUNT(r.rental_id) AS rentals
FROM film f
JOIN inventory i
ON f.film_id=i.film_id
JOIN rental r
ON i.inventory_id=r.inventory_id
GROUP BY f.title
ORDER BY rentals DESC
LIMIT 10;
""")

export_sheet(
    "Q14",
    """
    SELECT
        title,
        rentals
    FROM top_10_films;
    """
)

# ---------------------------------------
# Save Workbook
# ---------------------------------------

wb.save("sql_exercise_outputs.xlsx")

cursor.close()
conn.close()

print("Excel Export Completed Successfully!")
