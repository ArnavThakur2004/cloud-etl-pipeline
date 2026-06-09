-- Top Revenue Categories

SELECT
    Category,
    SUM("Net Sales") AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;


-- Most Profitable States

SELECT
    State,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 10;


-- Regional Performance

SELECT
    Region,
    SUM("Net Sales") AS Revenue,
    SUM(Profit) AS Profit
FROM sales
GROUP BY Region;


-- Average Delivery Time

SELECT
    AVG("Delivery Days")
FROM sales;

--Monthly Sales Trends  

-- Monthly Sales Trend

SELECT
    Year,
    Month,
    SUM("Net Sales") AS Revenue
FROM sales
GROUP BY Year, Month
ORDER BY Year, Month;