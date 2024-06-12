import networkx as nx
import numpy as np
import json
import random
import matplotlib.pyplot as plt
from pprint import pprint


def generate_random_graphs(min_size=2, max_size=20, num_graphs=100):
    graphs = []
    for _ in range(num_graphs):
        size = random.randint(min_size, max_size)
        prob = random.uniform(0, 1)
        G = nx.erdos_renyi_graph(size, prob)
        adj_matrix = nx.adjacency_matrix(G).todense()
        graphs.append(np.array(adj_matrix).tolist())
    return graphs


def save_to_json(graphs, file_name):
    with open(file_name, "w") as f:
        json.dump(graphs, f)


def load_from_json(file_name):
    with open(file_name, "r") as f:
        graphs = json.load(f)
    return graphs


def plot_graph(G, title="Graph"):
    plt.figure(figsize=(8, 8))
    nx.draw(
        G,
        node_size=700,
        node_color="lightblue",
        with_labels=True,
        font_weight="bold",
        edge_color="black",
    )
    plt.title(title)
    plt.show()


def plot_random_graph(n, p, directed=False, title="Random Graph"):
    G = nx.gnp_random_graph(n, p, directed=directed)
    plot_graph(G, title)


def get_graph_properties(G):
    properties = {
        "number_of_nodes": G.number_of_nodes(),
        "number_of_edges": G.number_of_edges(),
        "average_degree": (
            sum(dict(G.degree()).values()) / G.number_of_nodes()
            if G.number_of_nodes() > 0
            else 0
        ),
        "average_clustering_coefficient": nx.average_clustering(G),
        "diameter": nx.diameter(G) if nx.is_connected(G) else "Graph is not connected",
        "number_of_connected_components": nx.number_connected_components(G),
    }
    return properties


def analyze_graphs(graphs):
    all_properties = []
    for idx, adj_matrix in enumerate(graphs):
        G = nx.from_numpy_array(np.array(adj_matrix))
        properties = get_graph_properties(G)
        all_properties.append(properties)
        print(f"\nGraph {idx + 1} properties:")
        pprint(properties)
        print(f"Adjacency Matrix for Graph {idx + 1}:")
        print(np.array(adj_matrix))
    return all_properties


def summarize_properties(all_properties):
    summary = {
        "total_graphs": len(all_properties),
        "average_nodes": np.mean([prop["number_of_nodes"] for prop in all_properties]),
        "average_edges": np.mean([prop["number_of_edges"] for prop in all_properties]),
        "average_degree": np.mean([prop["average_degree"] for prop in all_properties]),
        "average_clustering_coefficient": np.mean(
            [prop["average_clustering_coefficient"] for prop in all_properties]
        ),
        "connected_graphs": sum(
            1 for prop in all_properties if prop["diameter"] != "Graph is not connected"
        ),
        "average_diameter_of_connected_graphs": np.mean(
            [
                prop["diameter"]
                for prop in all_properties
                if prop["diameter"] != "Graph is not connected"
            ]
        ),
        "average_connected_components": np.mean(
            [prop["number_of_connected_components"] for prop in all_properties]
        ),
    }
    return summary


def main():
    # Generate 100 random graphs with sizes between 2x2 and 20x20
    random_graphs = generate_random_graphs(num_graphs=100)

    # Save the adjacency matrices to a JSON file
    save_to_json(random_graphs, "random_graphs.json")
    print(f"Saved {len(random_graphs)} random graphs to 'random_graphs.json'")

    # Load the adjacency matrices from a JSON file
    graphs = load_from_json("random_graphs.json")
    print(f"Loaded {len(graphs)} random graphs from 'random_graphs.json'")

    # Analyze the generated graphs
    all_properties = analyze_graphs(graphs)

    # Summarize properties of all graphs
    summary = summarize_properties(all_properties)
    print("\nSummary of all graph properties:")
    pprint(summary)

    # Plot a simple undirected graph with 5 nodes
    # plot_random_graph(n=5, p=0.5, directed=False, title="Undirected Erdős-Rényi Random Graph with 5 Nodes")

    # Plot a simple directed graph with 5 nodes
    # plot_random_graph(n=5, p=0.5, directed=True, title="Directed Erdős-Rényi Random Graph with 5 Nodes")

    # Generate and analyze a specific graph
    # G = nx.erdos_renyi_graph(10, 0.3)
    # plot_graph(G, title="Specific Erdős-Rényi Graph with 10 Nodes and p=0.3")
    # properties = get_graph_properties(G)
    # print("Graph properties:")
    # pprint(properties)


if __name__ == "__main__":
    main()
