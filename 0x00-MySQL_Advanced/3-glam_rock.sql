-- Calculate the lifespan based on the 'formed' and 'split' columns
-- The lifespan is calculated as years from 'formed' to 'split'
-- Use 2022 as the reference year

SELECT band_name, 
       IFNULL(DATEDIFF(
           IF(splitted > 0, split, '2022-01-01'),
           formed), 0) as lifespan
FROM metal_bands
WHERE style LIKE '%GLAM ROCK%'
ORDER BY lifespan DESC;
