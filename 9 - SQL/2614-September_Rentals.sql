SELECT customers.name, rentals.rentals_date 
FROM customers, rentals
WHERE
(rentals.id_customers = customers.id) AND
EXTRACT(MONTH FROM rentals.rentals_date) = 09
