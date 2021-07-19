CREATE TABLE result AS

	(SELECT tours.*,
	 lat,
	 long
FROM tours
FULL OUTER Join cities
ON tours.city_id = cities.id
Where tours.city_id = cities.id);

SELECT * from result;




