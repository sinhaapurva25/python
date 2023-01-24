from scipy.signal import argrelextrema
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

array_dbp = np.array([])
for i in range(0, 10):
    dbp = i*2
    array_dbp = np.append(array_dbp, dbp)
m = argrelextrema(array_dbp, np.less())
print(array_dbp)

arr=np.array([1,2,3])
print(arr)


# defining the x and y arrays
y = np.array([1, 7, 4, 3, 9, 8, 0, 5, 3, 6, 4, 7, 8, 2, 4, 3, 0])
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
x = np.linspace(0,16, 17,True)

#Find peaks
peaks = find_peaks(y, height = 5, threshold = 1, distance = 1)
print(peaks)
peaks = find_peaks(y, height = 5, threshold = 1, distance = 2)
print(peaks)
height = peaks[1]['peak_heights'] #list of the heights of the peaks
print(height)
peak_pos = x[peaks[0]] #list of the peaks positions
print(peak_pos)

#Finding the minima
y2 = y*-1
minima = find_peaks(y2, height = 5, threshold = 1, distance = 1)
min_pos = x[minima[0]] #list of the minima positions
min_height = y2[minima[0]] #list of the mirrored minima heights

#Plotting
fig = plt.figure()
ax = fig.subplots()
ax.plot(x,y)
ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'D', label = 'Maxima')
ax.scatter(min_pos, min_height*-1, color = 'gold', s = 15, marker = 'X', label = 'Minima')
ax.legend()
ax.grid()
plt.show()