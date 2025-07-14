CREATE DATABASE airbnb;

USE airbnb;


CREATE TABLE listings (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    host_id BIGINT,
    host_name VARCHAR(100),
    neighbourhood_group VARCHAR(100),
    neighbourhood VARCHAR(100),
    latitude DECIMAL(10 , 6 ),
    longitude DECIMAL(10 , 6 ),
    room_type VARCHAR(50),
    price INT,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month DECIMAL(4 , 2 ),
    calculated_host_listings_count INT,
    availability_365 INT
);
