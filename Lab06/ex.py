import arviz as az
import matplotlib.pyplot as plt
import numpy as np

n_ore = 10
total_apeluri = 180

alpha_0 = 1.0
beta_0 = 0.05

alpha_post = alpha_0 + total_apeluri
beta_post = beta_0 + n_ore

mod = (alpha_post - 1) / beta_post
print(f"Distributia a posteriori: Gamma(alpha={alpha_post}, beta={beta_post})")
print(f"Modul calculat: {mod:.4f} apeluri/ora")

rng = np.random.default_rng(42)
samples = rng.gamma(shape=alpha_post, scale=1.0 / beta_post, size=200_000)

hdi_94 = az.hdi(samples, hdi_prob=0.94)
print(
    f"Intervalul HDI 94%: [{hdi_94[0]:.4f}, {hdi_94[1]:.4f}] apeluri/ora"
)

az.plot_posterior(
    samples,
    hdi_prob=0.94,
    point_estimate="mode",
    figsize=(8, 4),
)
plt.title(
    f"Distributia a posteriori Gamma({alpha_post}, {beta_post}) pentru λ"
)
plt.xlabel("Rata medie de apeluri pe ora (λ)")
plt.show()