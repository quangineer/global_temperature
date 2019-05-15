import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np 

city_temperature = "city_data_temperature.csv"
global_temperature = "global_data_temperature.csv"

#Name city_temperature (city level) data as data1 to read:
data1 = pd.read_csv(city_temperature)
#Name global_temperature (global level) data as data2 to read:
data2 = pd.read_csv(global_temperature)

# Seattle_temperature = list((data1[data1.city == 'Seattle'].avg_temp).fillna(0))
# print (Seattle_temperature)


Seattle_temperature = list(data1[data1.city == 'Seattle'].avg_temp)
for i in range(len(Seattle_temperature)):
    if str(Seattle_temperature[i]) == 'nan':
        Seattle_temperature[i] = 0

print (Seattle_temperature)


