import pandas as pd
import matplotlib.pyplot as plt


# baseDados = []
# with open("stops.txt", "r") as arquivo:
#     for registro in arquivo.readlines():
#         campos = registro.split(",")
#         camposLimpos = []
#         for item in campos:
#             item = item.replace("\n", "")
#             if (item.startswith("\"")):
#                 concat = item.strip()
#                 continue
#             elif (item.endswith("\"")):
#                 concat = f'{concat} {item.strip()}'
#                 camposLimpos.append(concat)
#             else:
#                 camposLimpos.append(item)
#         baseDados.append(camposLimpos)
#
# print(baseDados[0])
# print(baseDados[1])

# for campo in baseDados[1]:
#     print(campo)


data = pd.read_csv('dados/stops.txt')
data.head()
print(data.shape)

data.info()

id1_stop_lat = data[data.stop_lat==-23.541756]


print(id1_stop_lat)

plt.scatter(id1_stop_lat.stop_lat, id1_stop_lat.stop_lon)