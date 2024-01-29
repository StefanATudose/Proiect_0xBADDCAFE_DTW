import numpy as np
import matplotlib.pyplot as plt
from fastdtw import fastdtw
import time
from dtaidistance import dtw
from scipy.spatial.distance import euclidean
from pyts.metrics import dtw as pyts_dtw

time1 = np.linspace(0, 0.02, 3200)

s1 = np.sin(2*np.pi*800*time1)
s2 = np.sin(2*np.pi*800*time1 + np.pi/4)

dtw_time = time.time()
# [distanta, potriviri] = DTW(s1, s2)
distanta = pyts_dtw(s1, s2)
dtw_time = time.time() - dtw_time

print(f"DTW time: {dtw_time}")
print(f"DTW distance: {distanta}")

# # for pot in potriviri:
# #     plt.plot([pot[0], pot[1]], [s1[pot[0]], s2[pot[1]]], ':k')

# plt.plot(s1, color='blue', marker='o', markersize=10, linewidth=3)
# plt.plot(s2, color='red', marker='o', markersize=10, linewidth=3)


# plt.show()
# print(potriviri)

fastdw_time = time.time()
# print(s1.shape)
distance= pyts_dtw(s1, s2, method='fast', options={'radius': 10})
fastdw_time = time.time() - fastdw_time

print(f"Fast DTW time: {fastdw_time}")
print(f"Fast DTW distance: {distance}")

# fig, ax = plt.subplots()
# ax.plot(s1, label='A', color='red')
# ax.plot(s2, label='B', color='blue')

# for [map_x, map_y] in warp_path:
#     ax.plot([map_x, map_y], [s1[map_x], s2[map_y]], ':k')

# plt.show()