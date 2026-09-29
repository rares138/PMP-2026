import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az


bile_rosii = 0 

for i in range(1, 100001):
    urna = ['R', 'R', 'R', 'A', 'A', 'A', 'A', 'N', 'N']

    zar = np.random.randint(1,7)
    # print(zar)

    if zar == 2 or zar == 3 or zar == 5:
        urna.append('N')
    elif zar == 6:
        urna.append('R')
    else:
        urna.append('A')

    bila = np.random.choice(urna)
    # print(bila)
    # print(urna)
    if bila == 'R':
        bile_rosii = bile_rosii + 1

prob_r = bile_rosii / 100000
print(bile_rosii)
print(prob_r)