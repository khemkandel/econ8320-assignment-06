#si-exercise
import pandas as pd
import numpy as np

occupancy = pd.DataFrame()
occupancy = pd.read_csv('https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/roomOccupancy.csv')
occupancy.head(10)
occupancy['datatime'] = pd.to_datetime(occupancy['date'], format = "%Y-%m-%d %H:%M:%S")
occupancy.head()
occupancy['day_of_week'] =occupancy['datatime'].dt.day_name()
occupancy['hour'] =occupancy['datatime'].dt.hour
occupancy['minute'] =occupancy['datatime'].dt.minute
occupancy['bright'] = occupancy['Light'].map(lambda x: 1 if x > 0 else 0)
humidity_mean,light_mean = occupancy['Humidity'].mean(), occupancy['Light'].mean()
#print(str(humidity_mean)+ " "+str(light_mean))
occupancy['steamy'] = occupancy.apply(lambda row: 
    1 if row['Humidity'] > humidity_mean and row['Light'] > light_mean else 0, axis=1)
occupancy['Humidity'].mean()
occupancy['Light'].mean()
#df['Category'] = df.apply(lambda row: 'High Demand' if row['Sales'] > 500 and row['Region'] == 'North' else ('Moderate Demand' if row['Sales'] > 300 and row['Region'] == 'South' else 'Low Demand'), axis=1)
occupancy.head(100)