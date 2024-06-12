# GraphData

This repository contains a script to generate random graphs using the Erdős-Rényi model and analyze their properties. The script can generate random graphs of different sizes, save them as adjacency matrices in JSON format, and provide various statistics about the generated graphs.

## Table of Contents

- [GraphData](#graphdata)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Setup](#setup)
    - [Virtual Environment](#virtual-environment)
    - [Installing Requirements](#installing-requirements)
  - [Usage](#usage)
  - [Explanation of Graph Properties](#explanation-of-graph-properties)
    - [Number of Nodes](#number-of-nodes)
    - [Number of Edges](#number-of-edges)
    - [Average Degree](#average-degree)
    - [Average Clustering Coefficient](#average-clustering-coefficient)
    - [Diameter](#diameter)
    - [Number of Connected Components](#number-of-connected-components)
  - [License](#license)

## Description

The script in this repository generates random graphs with a specified range of sizes using the Erdős-Rényi model. It saves these graphs as adjacency matrices in a JSON file and provides detailed analysis of each graph's properties, such as the number of nodes, number of edges, average degree, average clustering coefficient, diameter, and number of connected components.

## Setup

### Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Here are the steps to set up a virtual environment:

1. Create a virtual environment:

   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

### Installing Requirements

After setting up the virtual environment, install the required packages using the `requirements.txt` file:

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate random graphs and analyze them, run the `random_graph_generator.py` script:

1. Generate random graphs and save them to a JSON file:

   ```bash
   python random_graph_generator.py
   ```

2. The script will output the properties of each graph and their adjacency matrices. It will also provide a summary of all graph properties.

## Explanation of Graph Properties

### Number of Nodes

- **Definition**: The number of nodes (or vertices) in the graph.
- **Explanation**: This tells you how many individual points there are in the graph. Each point represents a distinct entity.

### Number of Edges

- **Definition**: The number of edges (or connections) in the graph.
- **Explanation**: This tells you how many connections exist between pairs of nodes. An edge indicates a direct link between two nodes.

### Average Degree

- **Definition**: The average number of edges connected to each node.
- **Explanation**: This is calculated by taking the total number of edges connected to all nodes and dividing by the number of nodes. It gives an idea of how connected the graph is on average.
- **Formula**:
  \[
  \text{Average Degree} = \frac{\sum \text{degree of all nodes}}{\text{number of nodes}}
  \]

### Average Clustering Coefficient

- **Definition**: A measure of the degree to which nodes in a graph tend to cluster together.
- **Explanation**: This tells you how often nodes form tightly knit groups (clusters) where each node is connected to every other node in the group. A higher value indicates more clustering.
- **Range**: 0 to 1, where 0 means no clustering and 1 means perfect clustering.

### Diameter

- **Definition**: The longest shortest path between any two nodes in the graph.
- **Explanation**: This tells you the greatest distance (in terms of edges) between the furthest pair of nodes in the graph. It only applies if the graph is connected (there's a path between every pair of nodes).
- **Note**: If the graph is not connected, this property is reported as "Graph is not connected."

### Number of Connected Components

- **Definition**: The number of subgraphs in which any two nodes are connected to each other by paths.
- **Explanation**: This tells you how many separate groups of connected nodes exist within the graph. Each group is a connected component. If there is only one component, the entire graph is connected.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
