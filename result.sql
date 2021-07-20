CREATE TABLE result AS

	(SELECT tours.*,
	 lat,
	 long
FROM tours
FULL OUTER Join cities
ON tours.city_id = cities.id
Where tours.city_id = cities.id);

SELECT * from clean_tour_data;

ALTER TABLE result
RENAME TO clean_tour_data;



Create Table tour(
	id Serial primary key,
	city_id int,
	city varchar(40),
	state varchar(40),
	country varchar(40),
	year int,
	band varchar(50),
	lat varchar(10),
	long varchar(10)
)


Insert Into tour(city_id, city, state, country, year, band, lat, long)
Select * from clean_tour_data



Select * from tour




