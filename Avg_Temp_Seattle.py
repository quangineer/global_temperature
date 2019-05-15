import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib


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

# print (Seattle_temperature)

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

# print(running_mean(Seattle_temperature, 7))
A = running_mean(Seattle_temperature,7)

moving_average = A[6:]
# print (moving_average)

Year_to_Seattle_temperature = (list(data1[data1.city == 'Seattle'].year))[6:]
# print (Year_to_Seattle_temperature)

fig, ax = plt.subplots()
ax.plot(Year_to_Seattle_temperature, moving_average)

ax.set(xlabel='time (year)', ylabel='temperature (C)', title='Average Temperature in Seattle')
ax.grid()
fig.savefig("test.png")
plt.show()