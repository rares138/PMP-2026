import numpy as np
import random

p_bolnav = 0.01
p_bolnav_c = 0.99

p_poz_b = 0.95
p_neg_not_b = 0.90

p_b_poz = (p_poz_b * p_bolnav) / (p_poz_b * p_bolnav + (1 - p_neg_not_b) * p_bolnav_c)
print(p_b_poz)

nr = 100000

este_bolnav = np.random.choice([1, 0], p=[p_bolnav, p_bolnav_c], size=nr)

total_pozitivi = 0
pozitivi_si_bolnavi = 0

for om in este_bolnav:
    if om == 1:
        if random.random() < p_poz_b:
            total_pozitivi += 1
            pozitivi_si_bolnavi += 1
    else:
        if random.random() < (1 - p_neg_not_b):
            total_pozitivi += 1

print(pozitivi_si_bolnavi / total_pozitivi)