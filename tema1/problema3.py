import arviz as az
import matplotlib.pyplot as plt
import numpy as np

# scale = 1 / lambda
timpi_medii = [1/3, 1/6, 1/4]
prob = [3/13, 6/13, 4/13]

nr_clienti = 10000

frizeri_alesi = np.random.choice([0, 1, 2], size=nr_clienti, p=prob)

X = []
for frizer in frizeri_alesi:
    timp = np.random.exponential(scale=timpi_medii[frizer])
    X.append(timp)

X = np.array(X)

media = np.mean(X)
deviatia = np.std(X)

print("Media estimata a lui X:", media)
print("Deviatia standard a lui X:", deviatia)

# az.plot_kde(X)

# plt.show()