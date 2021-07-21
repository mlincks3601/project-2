CREATE TABLE cities (
    city    VARCHAR(40)     NOT NULL,
    state   VARCHAR(40)     NOT NULL,
    lat     VARCHAR (10)    NOT NULL,
	long    VARCHAR (10)    NOT NULL,
	id      INT             NOT NULL,
	PRIMARY KEY (id),
);
DROP TABLE tours;
CREATE TABLE tours (
    city_id      INT             NOT NULL,
	city    VARCHAR(40)     NOT NULL,
    state   VARCHAR(40)     NOT NULL,
    country VARCHAR (40)    NOT NULL,
	year    INT             NOT NULL,
	band    VARCHAR (50)    NOT NULL,
	FOREIGN KEY (city_id) REFERENCES cities (id)
);