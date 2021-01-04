import numpy as np
import random
import matplotlib.pyplot as plt

#
a = (0, 1, 1, 1, 2, 3, 7, 7, 23)

def count_elements(seq) -> dict:
"""Tally elements from `seq`."""
hist = {}
for i in seq:
    hist[i] = hist.get(i, 0) + 1
return hist

counted = count_elements(a)


def ascii_histogram(seq) -> None:
"""A horizontal frequency-table/histogram plot."""
counted = count_elements(seq)
for k in sorted(counted):
    print('{0:5d} {1}'.format(k, '+' * counted[k]))


random.seed(1)

vals = [1, 3, 4, 6, 8, 9, 10]
# Each number in `vals` will occur between 5 and 15 times.
freq = (random.randint(5, 15) for _ in vals)

data = []
for f, v in zip(freq, vals):
    data.extend([v] * f)

#`numpy.random` uses its own PRNG.
np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=10)
d[:5]
hist, bin_edges = np.histogram(d)
bcounts = np.bincount(a)
hist, _ = np.histogram(a, range=(0, max(a)), bins=max(a) + 1)
print(bcounts)
# Reproducing `collections.Counter`
print(
    "Reproducing `collections.Counter`:",
    dict(zip(np.unique(a), bcounts[bcounts.nonzero()])),
)


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()
