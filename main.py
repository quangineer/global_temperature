import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np


city_temperature = "city_data_temperature.csv"
global_temperature = "global_data_temperature.csv"


data1 = pd.read_csv(city_temperature)

data2 = pd.read_csv(global_temperature)

Seattle_temperature = list((data1[data1.city == 'Seattle'].avg_temp).fillna(0))

def running_mean(Seattle_temperature, N):
    sum = 0
    result = list( 0 for x in Seattle_temperature)

    for i in range(0, N):
        sum = sum + Seattle_temperature[i]
        result[i] = sum / (i+1)
    for i in range(N, len(Seattle_temperature)):
        sum = sum - Seattle_temperature[i-N] + Seattle_temperature[i]
        result[i] = sum/N
    return result 


A = (running_mean(Seattle_temperature,7))[6:]
Year_to_Seattle_temperature = (list(data1[data1.city == 'Seattle'].year))[6:]

Global_temperature = list(data2.avg_temp)
B = (running_mean(Global_temperature,7))[6:]
Year_to_Global_temperature = (list(data2.year))[6:]

fig, axs = plt.subplots()
plt.plot(Year_to_Global_temperature, B)
plt.plot(Year_to_Seattle_temperature, A)
fig.suptitle("Temperature Comparison between Seattle and the World over hundred years", fontsize=14)
axs.set_xlabel('time (year)')
axs.set_ylabel('temperature (Celsius)')
plt.legend(["Global", "Seattle"], loc='upper left')
plt.show()