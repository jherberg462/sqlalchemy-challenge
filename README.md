# API for weather data

## Goals

In this project, I wanted to create a flask app API that will query a SQLite database to return weather data in Hawaii.

## API/flask endpoints

Each route I created (except the base route) utilized SQLAlchemy to query a SQLite database. The base route displays a list of available routes. I created routes that return each dates precipitation, a list of weather stations used to gather data, and tempeture observations by date. I also created additional routes that will filter tempeture observations both by being after an input date, and between two input dates. 

## Deployment

I deployed my flask app at https://weather-api-492.herokuapp.com 
