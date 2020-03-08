#dependencies
import pandas as pd
import numpy as np
import datetime as dt
from sqlalchemy import create_engine, Column, Integer, String, Float, func, desc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify
import os

#path of sqlite file goes here in relation to current file
db_path = 'data/hawaii.sqlite'

#connect to sqllite db
engine = create_engine(f"sqlite:///{db_path}")



#reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

#set variable 'app' to run Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    welcome = '''
    /api/v1.0/precipitation</br>
    /api/v1.0/stations</br>
    /api/v1.0/tobs</br>
    /api/v1.0/< start> </br>
    /api/v1.0/< start>/< end> </br>
    
    '''

    return (welcome)




@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine) #connect to SQL file
    result = session.query(Measurement.date, Measurement.prcp).all() #run query
    session.close() #close connection
    results = [] #create empty list
    for date, precipitation in result:
        if precipitation == None: #clean data so that None is converted into 0
            precipitations = 0.0
        else:
            precipitations = precipitation
        result_dictionary = {} #create empty dictionary
        result_dictionary[date] = precipitations #make date the key and the prcp value the value
        results.append(result_dictionary) #append dictionary to the results list
    return jsonify(results)



@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    result = session.query(*[Measurement.station]).group_by(Measurement.station).    order_by(desc(func.count(Measurement.station))).all()
    session.close()
    result = list(np.ravel(result))
    return jsonify(result)
    


@app.route('/api/v1.0/tobs')
def temp():
    session = Session(engine)
    date_range = session.query(*[func.max(Measurement.date)]).all() #find latest date in dataset
    df_date_range = pd.DataFrame(date_range, columns=['date']) #put result into a df
    max_date = df_date_range.max()['date']
    dt_max_date = dt.datetime.strptime(max_date, '%Y-%m-%d') #get latest date in dataset into datetime object
    dt_year_before = dt_max_date + dt.timedelta(days=-365)
    year_before = dt.date.strftime(dt_year_before, '%Y-%m-%d')
    sel = [Measurement.tobs, Measurement.date] #list of columns to be selected
    result = session.query(*sel).filter(func.strftime('%Y-%m-%d', Measurement.date) >= year_before).    order_by(Measurement.date).all()
    session.close()
    results = []
    for temp, date in result:
        result_dictionary = {}
        result_dictionary[date] = temp
        results.append(result_dictionary)
    return jsonify(results)
    

@app.route('/api/v1.0/<start>')
def start(start):
    start = str(start)
    try:
        dt.datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        er = 'dates must be in yyyy-mm-dd format'
        return er
    session = Session(engine)
    temp_stats_sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), 
                      func.avg(Measurement.tobs), Measurement.date]
    result = session.query(*temp_stats_sel).filter(Measurement.date >= start).        group_by(Measurement.date).all()
    session.close()
    results = []
    for minimum, maximum, average, date in result:
        result_dictionary = {}
        results_dictionary = {}
        results_dictionary['min_temp'] = minimum
        results_dictionary['max_temp'] = maximum
        results_dictionary['average_temp'] = average
        result_dictionary[date] = results_dictionary
        results.append(result_dictionary)
    return jsonify(results)
    

@app.route('/api/v1.0/<start>/<end>')
def range(start, end):
    start = str(start)
    end = str(end)
    try:
        dt.datetime.strptime(start, '%Y-%m-%d')
        dt.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        er = 'dates must be in yyyy-mm-dd format'
        return er
    session = Session(engine)
    temp_stats_sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), 
                      func.avg(Measurement.tobs), Measurement.date]
    result = session.query(*temp_stats_sel).filter(Measurement.date >= start).        filter(Measurement.date <= end).group_by(Measurement.date).all()
    session.close()
    results = []
    for minimum, maximum, average, date in result:
        result_dictionary = {}
        results_dictionary = {}
        results_dictionary['min_temp'] = minimum
        results_dictionary['max_temp'] = maximum
        results_dictionary['average_temp'] = average
        result_dictionary[date] = results_dictionary
        results.append(result_dictionary)
    return jsonify(results)



#set debug to True for troubleshooting, keep troubleshooting code out of production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
