from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import networkx as nx
import matplotlib.pyplot as plt

model = BayesianNetwork([
    ('O', 'H'),
    ('O', 'W'),
    ('H', 'R'),
    ('W', 'R'),
    ('H', 'E'),
    ('R', 'C')
])

cpd_o = TabularCPD(
    variable='O',
    variable_card = 2,
    values=[[0.3], [0.7]],
    state_names = {'O': ['cold', 'mild']}
)

cpd_h = TabularCPD(
    variable='H',
    variable_card = 2,
    values=[[0.9, 0.2], [0.1, 0.8]],
    evidence=['O'],
    evidence_card=[2],
    state_names = {'H': ['yes', 'no'], 'O': ['cold', 'mild']}
)

cpd_w = TabularCPD(
    variable='W',
    variable_card = 2,
    values=[[0.1, 0.6], [0.9, 0.4]],
    evidence=['O'],
    evidence_card=[2],
    state_names = {'W': ['yes', 'no'], 'O': ['cold', 'mild']}
)

cpd_r = TabularCPD(
    variable='R',
    variable_card = 2,
    values=[[0.6,0.9,0.3,0.5],
            [0.4,0.1,0.7,0.5]],
    evidence=['H', 'W'],
    evidence_card=[2, 2],
    state_names = {'R': ['warm', 'cool'], 'H': ['yes', 'no'], 'W': ['yes', 'no']}
)

cpd_e = TabularCPD(
    variable='E',
    variable_card = 2,
    values=[[0.8, 0.2], [0.2, 0.8]],
    evidence=['H'],
    evidence_card=[2],
    state_names = {'E': ['high', 'low'], 'H': ['yes', 'no']}
)

cpd_c = TabularCPD(
    variable='C',
    variable_card = 2,
    values=[[0.85, 0.4], [0.15, 0.6]],
    evidence=['R'],
    evidence_card=[2],
    state_names = {'C': ['comfortable', 'uncomfortable'], 'R': ['warm', 'cool']}
)

model.add_cpds(cpd_o, cpd_h, cpd_w, cpd_r, cpd_e, cpd_c)

pos = nx.circular_layout(model)
nx.draw(model, with_labels=True, pos=pos, alpha=0.5, node_size=2000)
plt.show()

from pgmpy.inference import VariableElimination

infer = VariableElimination(model)

p_h_c = infer.query(variables=['H'], evidence={'C': 'comfortable'})
print(p_h_c)
p_e_c = infer.query(variables=['E'], evidence={'C': 'comfortable'})
print(p_e_c)
map_hw = infer.map_query(variables=['H', 'W'], evidence={'C': 'comfortable'})
print(map_hw)