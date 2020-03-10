# API for Hawaii weather data

The goal of this project was to create a flask app API that will query a SQLite database to retun weather data in Hawaii. The data is stored in a SQLite database, while SQLAlchemy was utilized to retreive and manipulate the data within the flask app. Analysis of the data, including visualizations was completed using Python libraries Pandas, Numpy and Matplotlib in a Jupyter Notebook. 

## Analysis Questions

1. How much precipitation did Hawaii get during the last year of my dataset?

2. Which weather stations had the most weather observations?

3. What are the most frequent tempeture observations recorded by the most active weather station over the last year of my dataset? 

4. Are the tempetures measured in the month of June statistically significantly different from the tempetures measued in the month of December? 

## Flask API endpoints

### Base Route

1. List of all available routes

### Static Routes

1. How much precipitation did Hawaii receive each day in my dataset?

2. Which weather stations are providing data in my dataset? 

3. What are the tempeture observations recorded in the last year of my dataset? 

### Dynamic Routes

1. What are the minimum, maximum and average tempetures from a given start date through the last date in my dataset?

2. What are the minimum, maximum and average tempetures in a given date range? 

## Tasks

### Analysis questions

1. Connect to SQLite Database ("DB") using SQLAlchemy, and reflect the tables.

2. Calculate the latest date in my dataset, and use this to calculate the last year in my dataset.

3. Use SQLAlchemy to query DB to find the amount of precipitation and the date, filterd by the date range in step 2 above. 

4. Plot results from step 3 above into a Matplotlib chart

5. Use SQLAlchemy to query DB to find the Weather Station ID, and how many rows each Weather Station ID appears in, and order the results by how many rows each Weather Station ID appears in. 

6. Modify the query in step 6 above to return only the first result, and save only the Weather Station ID into a variable

7. Use SQLAlchemy to query the DB to find the date and tempature, filtered by the Weather Station ID found in step 6 above, and by the date range found in step 2 above. 

8. Use Matplotlib to show the tempeture and frequency of the tempeture, grouped into 12 bins. 

9. Create two DB queries that find the Weather Station ID, and the average observed tempeture, grouped by the Weather Station ID, one that filters by the measurement date being in June, and one that filters by the measurement date being in December

10. Create a for loop that loops through the results of both queries in step 9 above, and appends the average observed tempeture into a list. 

11. Run a t-test to determine if the tempetures in December are the same as the tempetures as in June. 

12. Review results from step 11 above to determine if the null hypothesis can be rejected

## Flask API endpoints

### Base Route

1. Define a route and corresponding function that returns text listing all of the API endpoints

### Static Routes

#### How much precipitation did Hawaii get during the last year of my dataset?

1. Define flask route and corresponding function

2. within the function defined in step 1 above, connect to the DB, **continue here


## API/flask endpoints

Each route I created (except the base route) utilized SQLAlchemy to query a SQLite database. The base route displays a list of available routes. I created routes that return each dates precipitation, a list of weather stations used to gather data, and tempeture observations by date. I also created additional routes that will filter tempeture observations both by being after an input date, and between two input dates. 

## Deployment

I deployed my flask app at https://weather-api-492.herokuapp.com 



