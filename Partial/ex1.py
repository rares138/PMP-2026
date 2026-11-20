from hmmlearn import hmm
import numpy as np

states = [1,2,3,4]
obs = ['R', 'G', 'B']

pi = np.array([1/4,1/4,1/4,1/4])

A = np.array([
    [0.2,0.4,0,0.4],
    [0.4,0.2,0.4,0],
    [0,0.4,0.2,0.4],
    [0.4,0,0.4,0.2],
])

B = np.array([
    [0.7,0.2,0.1],
    [0.2,0.6,0.2],
    [0.1,0.3,0.6],
    [0.5,0.2,0.3]
])

obs_seq = ['R', 'G', 'B', 'B', 'R']
obs_map = {'R' : 0, 'G': 1, 'B': 2}
secventa_observata = [obs_map[i] for i in obs_seq]

# hmm_model = hmm.MultinomialHMM(n_components=len(states))
# hmm_model.startprob_ = pi
# hmm_model.transmat_ = A
# hmm_model.emissionprob_ = B

def myViterbi(pi, A, B, sir):
  N = len(pi)
  T = len(sir)
  delta = np.zeros((T, N))
  psi = np.zeros((T,N), dtype=int)

  delta[0] = pi * B[:, sir[0]]

  for t in range(1, T):
      for j in range(N):
          options = delta[t-1]*A[:,j]
          delta[t,j] = B[j, sir[t]]*np.max(options)
          psi[t,j] = np.argmax(options)
  return delta, psi

d, p = myViterbi(pi, A, B, secventa_observata)
print(d[0])
print(d[1])
print(d[2])
print(d[3])
print("Cea mai probabila secventa de stari: ", p)
print("Probabilitatea secventei observate: ", np.max(d[-1]))

A2 = np.array([
    [0.25,0.25,0.25,0.25],
    [0.25,0.25,0.25,0.25],
    [0.25,0.25,0.25,0.25],
    [0.25,0.25,0.25,0.25],
])

d2, p2 = myViterbi(pi, A2, B, secventa_observata)
print(d2[0])
print(d2[1])
print(d2[2])
print(d2[3])
print("Cea mai probabila secventa de stari: ", p2)
print("Probabilitatea secventei observate: ", np.max(d2[-1]))
