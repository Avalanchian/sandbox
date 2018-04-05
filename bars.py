#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
milgram_obj = open("/home/matthew/sandbox/milgram.txt")
milgram_raw = milgram_obj.read()
milgram_obj.close()
milgram_list = milgram_raw.splitlines()
data = [i.split() for i in milgram_list]
voltages = [milgram_list[i][0] for i in range(len(milgram_list))]
percent = [milgram_list[i][1] for i in range(len(milgram_list))]

x = 
num_bins = len(milgram_list)

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins, density=1)

plt.show()
"""
"""
t = np.arange(0.0, 1.0, 0.01)
v = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, v)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='A simple sin curve')
#ax.grid()

fig.savefig('test.png')
plt.show()"""


line = plt.figure()

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "x")
plt.show()
