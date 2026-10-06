'''
a) sansa ca jocul sa se termine din primul pas:
    P(N=1) = 1/2 = 0.5
   sansa ca jocul sa se termine din al doilea pas:
    P(N=2) = 1/2 * 1/2 = 1/4 = 0.25
   sansa ca jocul sa se termine din al treilea pas:
    P(N=3) = 1/2 * 1/2 * 1/2 = 1/8 = 0.125

    Este distributie geometrica, la fiecare pas probabilitatea se injumateste.
'''

import random
import matplotlib.pyplot as plt

def joc_b():
    N = 0
    S = 0.0

    while True:
        N = N+1
        moneda = random.choice(["stema", "ban"])
        if moneda == "stema":
            zar = random.randint(1, 6)
            S = S + (zar - 3)
            break
        else:
            S = S - 0.5

    print("Jocul s-a terminat")
    print("Numarul de pasi:", N)
    print("Suma:", S)

# joc_b()

def joc_c(p_stema=0.5):
    N = 0
    S = 0.0
    while True:
        N = N+1
        if random.random() < p_stema:
            zar = random.randint(1, 6)
            S = S + (zar - 3)
            break
        else:
            S = S - 0.5
    return N, S

sume = []
for _ in range(10000):
    N, S = joc_c()
    sume.append(S)

print("Media pentru p_stema=0.5:", sum(sume)/len(sume))

plt.hist(sume, edgecolor='black')
plt.show()

# d) moneda masluita cu p_stema=0.3 si p_stema=0.7
sume_03 = []
for _ in range(10000):
    N, S = joc_c(p_stema=0.3)
    sume_03.append(S)

print("Media pentru p_stema=0.3:", sum(sume_03)/len(sume_03))

plt.hist(sume_03, color='lightblue', edgecolor='black')
plt.show()

sume_07 = []
for _ in range(10000):
    N, S = joc_c(p_stema=0.7)
    sume_07.append(S)

print("Media pentru p_stema=0.7:", sum(sume_07)/len(sume_07))

plt.hist(sume_07, color='darkblue', edgecolor='black')
plt.show()