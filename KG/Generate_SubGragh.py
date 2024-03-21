import json
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm  # Import tqdm library

# Load the knowledge graph from the JSON file
with open('KG/KG/ruby_knowledge_graph_with_edges.json', 'r') as json_file:
    graph_data = json.load(json_file)
    knowledge_graph = nx.node_link_graph(graph_data)

# Extract connected components (subgraphs)
connected_components = list(nx.connected_components(knowledge_graph))

# Iterate over each subgraph
for i, component in tqdm(enumerate(connected_components, 1), total=len(connected_components), desc="Processing Subgraphs"):
    # Check if the subgraph has more than two nodes
    if len(component) > 1:
        subgraph = knowledge_graph.subgraph(component)
        
        # Save the subgraph as a JSON file
        subgraph_data = nx.node_link_data(subgraph)
        subgraph_json_str = json.dumps(subgraph_data, indent=4)

        with open(f'KG/SubGraph/all/ruby_subgraph_{i}.json', 'w') as subgraph_json_file:
            subgraph_json_file.write(subgraph_json_str)
