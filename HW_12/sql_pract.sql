SELECT *
FROM employees;
-----------------------
SELECT DISTINCT first_name, last_name, city
FROM employees;
-----------------------
SELECT DISTINCT first_name, city, country, title
FROM employees;
--------------------------
SELECT DISTINCT company_name, city, address, country
FROM customers;
--------------------------
SELECT COUNT (DISTINCT customer_id)
FROM orders;
--------------------------
SELECT COUNT (DISTINCT ship_name)
FROM orders;
--------------------------
SELECT COUNT (ship_city)
FROM orders;
--------------------------
SELECT COUNT (DISTINCT ship_city)
FROM orders;
-------------------------
SELECT company_name, contact_name, phone
FROM customers
WHERE country = 'USA';
-------------------------
SELECT company_name, contact_name, phone
FROM customers
WHERE country = 'UK';
-------------------------
SELECT *
FROM products
WHERE unit_price > 20;
-------------------------
SELECT *
FROM products
WHERE unit_price <> 2;
-------------------------
SELECT COUNT (*)
FROM products
WHERE unit_price > 20;
-------------------------
SELECT *
FROM products
WHERE discontinued = 1;
-------------------------
SELECT *
FROM products
WHERE discontinued < 1;
-------------------------
SELECT *
FROM customers
WHERE city != 'Berlin';
-------------------------
SELECT *
FROM orders
WHERE order_date > '1996-07-04';
-------------------------
SELECT *
FROM products
WHERE unit_price > 25 and units_in_stock > 40;
-------------------------