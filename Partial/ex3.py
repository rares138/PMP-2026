alpha_prior = 2
beta_prior = 8
produse = 20
defecte = 5

alpha_post = alpha_prior + defecte
beta_post = beta_prior + (produse - defecte)

from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)

plt.figure(figsize=(8, 4.5))
plt.plot(x, beta.pdf(x, alpha_prior, beta_prior), label=f'A priori: Beta({alpha_prior}, {beta_prior})', linestyle='--')
plt.fill_between(x, beta.pdf(x, alpha_prior, beta_prior), alpha=0.15)

plt.plot(x, beta.pdf(x, alpha_post, beta_post), label=f'A posteriori: Beta({alpha_post}, {beta_post})', linewidth=2)
plt.fill_between(x, beta.pdf(x, alpha_post, beta_post), alpha=0.25)

plt.title('A priori vs. A posteriori')
plt.xlabel('Probabilitatea (p)')
plt.ylabel('Densitate de probabilitate')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

alpha_post = alpha_prior + 3
beta_post = beta_prior + (15 - 3)

x = np.linspace(0, 1, 500)

plt.figure(figsize=(8, 4.5))
plt.plot(x, beta.pdf(x, alpha_prior, beta_prior), label=f'A priori: Beta({alpha_prior}, {beta_prior})', linestyle='--')
plt.fill_between(x, beta.pdf(x, alpha_prior, beta_prior), alpha=0.15)

plt.plot(x, beta.pdf(x, alpha_post, beta_post), label=f'A posteriori: Beta({alpha_post}, {beta_post})', linewidth=2)
plt.fill_between(x, beta.pdf(x, alpha_post, beta_post), alpha=0.25)

plt.title('A priori vs. A posteriori')
plt.xlabel('Probabilitatea (p)')
plt.ylabel('Densitate de probabilitate')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
