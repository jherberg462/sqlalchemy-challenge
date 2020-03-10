# API for Hawaii weather data

The goal of this project was to create a flask app API that will query a SQLite database to retun weather data in Hawaii. The data is stored in a SQLite database, while SQLAlchemy was utilized to retreive and manipulate the data within the flask app. Analysis of the data, including visualizations was completed using Python libraries Pandas, Numpy and Matplotlib in a Jupyter Notebook. 

## Analysis Questions

1. How much precipitation did Hawaii get during the last year of my dataset?

2. Which weather stations had the most weather observations?

3. What are the most frequent tempeture observations recorded by the most active weather station over the last year of my dataset? 

4. Are the tempetures measured in the month of June statistically significantly different from the tempetures measued in the month of December? 

## Flask API endpoints

### Base Route



## API/flask endpoints

Each route I created (except the base route) utilized SQLAlchemy to query a SQLite database. The base route displays a list of available routes. I created routes that return each dates precipitation, a list of weather stations used to gather data, and tempeture observations by date. I also created additional routes that will filter tempeture observations both by being after an input date, and between two input dates. 

## Deployment

I deployed my flask app at https://weather-api-492.herokuapp.com 



