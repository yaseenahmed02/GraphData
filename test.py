import networkx as nx
import matplotlib.pyplot as plt

# Parameters for the undirected graph
n = 10  # Number of nodes
p = 0.5  # Probability of edge creation

# Generate an undirected random graph using the G(n, p) model
G_undirected = nx.erdos_renyi_graph(n, p)

# Plot the undirected graph
plt.figure(figsize=(8, 8))
nx.draw(
    G_undirected,
    node_size=700,
    node_color="lightblue",
    with_labels=True,
    font_weight="bold",
    edge_color="black",
)
plt.title("Undirected Erdős-Rényi Random Graph G(n, p) with 5 Nodes")
plt.show()
