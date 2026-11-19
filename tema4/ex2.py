from pgmpy.models import DiscreteMarkovNetwork as MNModel
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import DiscreteFactor
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

weather_states = ['Soare', 'Ploaie', 'Nori']

# n = 4, S1 - S2 - S3, S2 - S4
mrf_weather = MNModel([('S1', 'S2'), ('S2', 'S3'), ('S2', 'S4')])

# factori unari pentru fiecare statie
p_init = np.array([0.5, 0.3, 0.2])
for i in ['S1', 'S2', 'S3', 'S4']:
    p = DiscreteFactor([i], cardinality=[3], values=p_init)
    mrf_weather.add_factors(p)

Psi = np.array([
    [0.7, 0.2, 0.1],
    [0.2, 0.6, 0.2],
    [0.1, 0.3, 0.6]
])

for u, v in mrf_weather.edges():
    p = DiscreteFactor([u, v], cardinality=[3, 3], values=Psi.flatten())
    mrf_weather.add_factors(p)

G = nx.Graph()
G.add_nodes_from(mrf_weather.nodes())
G.add_edges_from(mrf_weather.edges())

print("Este arbore (fără cicluri)?:", nx.is_tree(G))
for node in G.nodes():
  print(f"Vecinii lui {node}: {list(G.neighbors(node))}")

plt.figure(figsize=(5, 4))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    font_weight="bold",
)
plt.title("Graful MRF al statiilor meteo")
plt.show()

infer = VariableElimination(mrf_weather)

# presupunem ca la S1 este Ploaie (1) si la S3 este Nori (2). Calculam distributia marginala la S2 si S4:
q_S2 = infer.query(variables=['S2'], evidence={'S1': 1, 'S3': 2})
q_S2.normalize()
print("\nDistributia marginala la S2 dat fiind S1=Ploaie, S3=Nori:")
print(q_S2)
map_S2 = weather_states[int(np.argmax(q_S2.values))]
print("   Starea MAP marginala la S2:", map_S2)

# configuratia comuna MAP a tuturor statiilor neobservate (S2, S4):
q_S4 = infer.query(variables=["S4"], evidence={'S1': 1, 'S3': 2})
q_S4.normalize()
map_S4 = weather_states[int(np.argmax(q_S4.values))]
print(f"\nMaxime marginale separate: S2={map_S2}, S4={map_S4}")

map_joint = infer.map_query(variables=["S2", "S4"], evidence={'S1': 1, 'S3': 2})
print(
    "Configuratia comuna MAP pentru (S2, S4):",
    {k: weather_states[v] for k, v in map_joint.items()},
)