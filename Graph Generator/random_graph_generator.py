import os
import networkx as nx
import numpy as np
import json
import random
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


def generate_degree_descriptions(G):
    descriptions = []
    for node, degree in dict(G.degree()).items():
        neighbors = list(G.neighbors(node))
        neighbor_str = ", ".join(map(lambda x: f"Node {x+1}", neighbors))
        descriptions.append(
            f"Node {node+1} has {degree} connections: {neighbor_str}.")
    return descriptions


def generate_neighborhood_descriptions(G):
    descriptions = []
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        descriptions.append(
            f"Node {node+1} is adjacent to nodes {', '.join(map(lambda x: str(x+1), neighbors))}."
        )
    return descriptions


def generate_shortest_path_descriptions(G):
    descriptions = []
    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                try:
                    path = nx.shortest_path(G, source=source, target=target)
                    path_desc = " -> ".join(map(lambda x: str(x + 1), path))
                    descriptions.append(
                        f"The shortest path from node {source+1} to node {target+1} is through nodes {path_desc}."
                    )
                except nx.NetworkXNoPath:
                    descriptions.append(
                        f"There is no path from node {source+1} to node {target+1}."
                    )
    return descriptions


def generate_component_descriptions(G):
    descriptions = []
    for component in nx.connected_components(G):
        descriptions.append(
            f"Nodes {', '.join(map(lambda x: str(x+1), component))} form a connected component."
        )
    return descriptions


def generate_connection_descriptions(G):
    descriptions = []
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        descriptions.append(
            f"Node {node+1} is connected to nodes {', '.join(map(lambda x: str(x+1), neighbors))}."
        )
    return descriptions


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


def save_graph_data(graph_idx, adj_matrix, descriptions, properties, base_dir="GDL"):
    os.makedirs(base_dir, exist_ok=True)

    graph_data = {
        "adjacency_matrix": adj_matrix,
        "properties": properties,
        "descriptions": descriptions,
    }

    with open(os.path.join(base_dir, f"graph_{graph_idx+1}.json"), "w") as f:
        json.dump(graph_data, f, indent=4)


def main():
    # Generate 100 random graphs with sizes between 2x2 and 20x20
    random_graphs = generate_random_graphs(num_graphs=100)

    # Save the adjacency matrices to a JSON file
    save_to_json(random_graphs, "random_graphs.json")
    print(f"Saved {len(random_graphs)} random graphs to 'random_graphs.json'")

    # Load the adjacency matrices from a JSON file
    graphs = load_from_json("random_graphs.json")
    print(f"Loaded {len(graphs)} random graphs from 'random_graphs.json'")

    # Analyze and describe the generated graphs
    for idx, adj_matrix in enumerate(graphs):
        G = nx.from_numpy_array(np.array(adj_matrix))
        properties = get_graph_properties(G)

        descriptions = {
            "degree_descriptions": generate_degree_descriptions(G),
            "neighborhood_descriptions": generate_neighborhood_descriptions(G),
            "shortest_path_descriptions": generate_shortest_path_descriptions(G),
            "component_descriptions": generate_component_descriptions(G),
            "connection_descriptions": generate_connection_descriptions(G),
        }

        save_graph_data(idx, adj_matrix, descriptions, properties)
        print(f"Saved data for graph {idx + 1}")


if __name__ == "__main__":
    main()
