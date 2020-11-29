import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import math

data = np.genfromtxt('www/data/raw_data.csv', delimiter=',',skip_header=1, dtype=[('Time','f8'),('Latency','f8')])

# Generate some test data
x = data['Time']
y = data['Latency']

x_bins = math.ceil(max(x) - min(x))
print(x_bins)
# density=True, 
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[x_bins, 60], density=True)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

fig = plt.figure()
ax = fig.gca()

ax.imshow(heatmap.T, cmap='turbo', origin='lower', extent=extent, aspect='auto')

fig.tight_layout()

fig.savefig("output.png")