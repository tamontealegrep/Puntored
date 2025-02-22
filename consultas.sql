-- 1. Obtener los 5 clientes con mayor monto total de ventas en los últimos 6 meses
SELECT c.id, c.nombre, c.apellido, COALESCE(SUM(v.monto), 0) AS total_ventas
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY c.id, c.nombre, c.apellido
ORDER BY total_ventas DESC
LIMIT 5;

-- 2. Calcular el ticket promedio de ventas por cliente en el último año
SELECT c.id, c.nombre, c.apellido, COALESCE(AVG(v.monto), 0) AS ticket_promedio
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.id, c.nombre, c.apellido;

-- 3. Obtener el nombre completo de los clientes y su monto total de ventas
SELECT c.id, CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo, COALESCE(SUM(v.monto), 0) AS total_ventas
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
GROUP BY c.id, c.nombre, c.apellido
ORDER BY total_ventas DESC;

-- 4. Obtener el ingreso promedio de ventas por mes
SELECT EXTRACT(YEAR FROM v.fecha) AS año, EXTRACT(MONTH FROM v.fecha) AS mes, COALESCE(AVG(v.monto), 0) AS ingreso_promedio
FROM ventas v
WHERE v.fecha >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY EXTRACT(YEAR FROM v.fecha), EXTRACT(MONTH FROM v.fecha)
ORDER BY año DESC, mes DESC;

-- 5. Calcular el ranking de clientes por ventas en el último año
SELECT c.id, CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo, COALESCE(SUM(v.monto), 0) AS total_ventas,
    RANK() OVER (ORDER BY COALESCE(SUM(v.monto), 0) DESC) AS ranking
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.id, c.nombre, c.apellido
ORDER BY ranking;

-- 6. Calcular el total de ventas por cliente y seleccionar solo los clientes cuyo total de ventas es superior al promedio general
SELECT c.id, CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo, COALESCE(SUM(v.monto), 0) AS total_ventas
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
GROUP BY c.id, c.nombre, c.apellido
HAVING COALESCE(SUM(v.monto), 0) > (
    SELECT AVG(total_sales)
    FROM (
        SELECT COALESCE(SUM(v2.monto), 0) AS total_sales
        FROM ventas v2
        GROUP BY v2.cliente_id
    ) AS sales_per_customer
)
ORDER BY total_ventas DESC;
