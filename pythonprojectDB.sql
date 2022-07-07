CREATE DATABASE pythonproject;

USE pythonproject;

CREATE TABLE song (
id int PRIMARY KEY NOT NULL IDENTITY(1,1),
songname varchar(45),
duration time,
genre varchar(45),
);

CREATE TABLE artist (
id int PRIMARY KEY NOT NULL IDENTITY(1,1),
name varchar(45),
gender VARCHAR(10) NOT NULL CHECK (Gender IN ('Male','Female')),
date_of_creation date
);

DROP TABLE artist;