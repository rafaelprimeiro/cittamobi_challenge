import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stops.txt')
data.head()
print(data.shape)

data.info()

id1_stop_lat = data[data.stop_lat==-23.541756]


print(id1_stop_lat)

plt.scatter(id1_stop_lat.stop_lat, id1_stop_lat.stop_lon)