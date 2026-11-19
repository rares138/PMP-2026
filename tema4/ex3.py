import matplotlib.pyplot as plt
import numpy as np

x_original = np.zeros((5, 5), dtype=int)
x_original[1:4, 1:4] = 1

print("Matricea originală (x):")
print(x_original)

plt.figure(figsize=(3.5, 3.5))
plt.imshow(x_original, cmap="gray", vmin=0, vmax=1)
plt.title("Imaginea originală (x)")
plt.xticks(range(5))
plt.yticks(range(5))
plt.show()

np.random.seed(42)



zgomot_mask = np.random.rand(5, 5) < 0.1
y_observat = x_original.copy()
y_observat[zgomot_mask] = 1 - y_observat[zgomot_mask]

print(f"Pixeli modificați: {zgomot_mask.sum()} din {x_original.size}")
print("Matricea observată cu zgomot (y):")
print(y_observat)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

axes[0].imshow(x_original, cmap="gray", vmin=0, vmax=1)
axes[0].set_title("Imaginea originală (x)")
axes[0].set_xticks(range(5))
axes[0].set_yticks(range(5))

axes[1].imshow(y_observat, cmap="gray", vmin=0, vmax=1)
axes[1].set_title("Imaginea cu zgomot (y)")
axes[1].set_xticks(range(5))
axes[1].set_yticks(range(5))

plt.tight_layout()
plt.show()