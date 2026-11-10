import pymc as pm
import arviz as az
import numpy as np
data = np.array([56, 60, 58, 55, 57, 59, 61, 56, 58, 60])
x = np.mean(data)
with pm.Model() as model:
    mu = pm.Normal("mu", mu=x, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=10)
    y = pm.Normal("y", mu=mu, sigma=sigma, observed=data)
    idata = pm.sample(draws=1000, tune=1000, chains=4, random_seed=42)

print(model.str_repr())
print(az.summary(idata, hdi_prob=0.95))