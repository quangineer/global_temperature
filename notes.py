#how to replace Nan Values with Zero in Pandas DataFrame:

#df: the "big" file of data after reading csv file

# For a single column using pandas:
df['DataFrame Column'] = df['DataFrame Column'].fillna(0)
Seattle_temperature = list((data1[data1.city == 'Seattle'].avg_temp).fillna(0))
# For a single column using numpy:
df['DataFrame Column'] = df['DataFrame Column'].replace(np.nan,0)
Seattle_temperature = list((data1[data1.city == 'Seattle'].avg_temp).replace(np.nan,0))
# For an entire DataFrame using pandas:
df.fillna(0)
Seattle_temperature = data1.fillna(0)
# For an entire DataFrame using numpy:
df.replace(np.nan,0)
Seattle_temperature = data1.replace(np.nan,0)


# Utilize purely PYTHON to solve the problem above:
Seattle_temperature = list(data1[data1.city == 'Seattle'].avg_temp)
for i in range(len(Seattle_temperature)):
    if str(Seattle_temperature[i]) == 'nan':
        Seattle_temperature[i] = 0
        # 'nan' is  a string here. Thus to compare with it, we need 
        # to make a string for the other side of the equal comparison.

#when using loop (for i in Varible), if we use Variable, it will 
#create a new list separatedly from the list we loop. Be careful
# when print this loop result as it may not show the changed list
# (instead, it will show the unchanged statu quo list)

#It is kind of sort and sorted when sort does not make a new list
#  and only change within the given list. Otherwise, sorted make a 
#  new list differentiating itself from the provided list.