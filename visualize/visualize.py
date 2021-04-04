import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import math
import sys

data = np.genfromtxt(sys.stdin, delimiter=',', dtype=[('Time','f8'),('Latency','f8')])

# filter out first and last second to remove outliers
data = data[(data['Time'] >= min(data['Time']) + 1) & (data['Time'] <= max(data['Time']) - 1)]

x = data['Time']
y = data['Latency']

x -= min(x)

x_bins = math.ceil(max(x) - min(x) + 1)
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[x_bins, 50])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Normalize the heatmap so that sum of every row is 1
sum_of_rows = heatmap.sum(axis=1)
normalized_heatmap = heatmap / sum_of_rows[:, np.newaxis]

hist_bins = [xedges[0] + i for i in range(len(sum_of_rows)+1)]

print(heatmap.T)
print(extent)

print(hist_bins)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10,10))

axes[0].set_title("Latency heatmap")
axes[0].imshow(normalized_heatmap.T, cmap='turbo', origin='lower', extent=extent, aspect='auto')
axes[0].set_ylabel("Latency (s)")

axes[1].hist(x=x, bins=hist_bins)
axes[1].set_title("Throughput")
axes[1].set_ylabel("Throughput (req/s)")
axes[1].set_xlabel("Time (s)")
axes[1].set_xlim(hist_bins[0], hist_bins[-1])

fig.tight_layout()

fig.savefig(sys.stdout.buffer)