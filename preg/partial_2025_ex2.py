import numpy as np
from hmmlearn import hmm

states = ['W', 'R', 'S']
obs = ['L', 'M', 'H']

pi = np.array([0.4, 0.3, 0.3])

A = np.array([
    [0.6,0.3,0.1],
    [0.2,0.7,0.1],
    [0.3,0.2,0.5]
])

B = np.array([
    [0.1,0.7,0.2],
    [0.05,0.25,0.7],
    [0.8,0.15,0.05]
])

hmm_model = hmm.MultinomialHMM(n_components=len(states))
hmm_model.startprob_ = pi
hmm_model.transmat_ = A
hmm_model.emissionprob_ = B

obs_map = {'L': 0, 'M': 1, 'H': 2}
obs_seq = [obs_map[i] for i in ['M', 'H', 'L']]
log_ver = hmm_model.score(np.array(obs_seq))
fwd = np.exp(log_ver)

# alt: Implementare explicita a algoritmului Forward in numpy (pentru afisarea tabelului alpha)
def forward_algorithm(pi, A, B, obs_indices):
    T = len(obs_indices)
    N = len(pi)
    alpha = np.zeros((T, N))
    # Initializare (t = 0)
    alpha[0] = pi * B[:, obs_indices[0]]
    # Recurenta (t = 1 .. T-1)
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = B[j, obs_indices[t]] * np.sum(alpha[t - 1] * A[:, j])
    return alpha, np.sum(alpha[-1])

alpha_table, prob_forward_manual = forward_algorithm(pi, A, B, [1, 2, 0])

print("Algoritmul Forward pentru secventa [Medium, High, Low]:")
print("Tabelul alpha_t(j):")
for t, row in enumerate(alpha_table):
    print(f"  t={t+1}: W={row[0]:.6f}, R={row[1]:.6f}, S={row[2]:.6f}")
print(f"=> Probabilitatea exacta P(O = [M, H, L]) (hmmlearn): {fwd:.6f}")
print(f"=> Probabilitatea exacta P(O = [M, H, L]) (manual):   {prob_forward_manual:.6f}\n")

# print(hmm_model.predict(np.array(obs_seq), algorithm="viterbi"))

target_seq = [1,2,0]
n = 10000
cnt = 0
for i in range(n):
    X, Z = hmm_model.sample(n_samples=3)
    if list(X.flatten()) == target_seq:
        cnt = cnt + 1

empirical_prob = cnt / n
print(empirical_prob)