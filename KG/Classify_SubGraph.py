import os
import json

# DFS implementation for extracting four types of subgraphs

def dfs(graph, start, visited, component):
    visited.add(start)
    component.append(start)
    for neighbor in graph.get(start, []):  # Use the .get() method to get the list of neighboring nodes, returns an empty list if the node does not exist
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    return components

def extract_nodes_info(graph, connected_component, original_data):
    nodes_info = []
    for node_id in connected_component:
        for node in original_data['nodes']:
            if node['package_id'] == node_id:
                nodes_info.append(node)
                break
    return nodes_info

def classify(input_folder,output_folder,edge_properties):
    # Read all JSON files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            # Build the complete path of the JSON file
            input_file_path = os.path.join(input_folder, filename)
            
            # Read the JSON file
            with open(input_file_path, 'r') as file:
                original_data = json.load(file)
            
            # Build the graph
            graph = {}
            for node in original_data['nodes']:
                node_id = node['package_id']
                neighbors = []
                for prop in edge_properties:
                    neighbors = neighbors + node.get(prop, [])
                graph[node_id] = neighbors
            
            # Find connected components
            connected_components = find_connected_components(graph)
            
            # Output the node information of each connected component to a JSON file
            for idx, component in enumerate(connected_components, start=1):
                component_nodes_info = extract_nodes_info(graph, component, original_data)
                if len(component_nodes_info) > 1:
                    output_data = {'nodes': component_nodes_info}
                    output_file_path = os.path.join(output_folder, f'component_{idx}_{filename}')
                    with open(output_file_path, 'w') as outfile:
                        json.dump(output_data, outfile, indent=4)


# input_folder: Path to folder containing input JSON files representing graphs.
# output_folder: Path to folder where output JSON files will be saved, each containing node information of connected components.
# edge_properties: List of edge properties to extract from input JSON files for building the graph.

# ruby as example
input_folder = 'KG/SubGraph/all'
output_folder = 'KG/SubGraph/SG'

# DG
# edge_properties = ['edge_codehash', 'edge_name']
# # DeG
# edge_properties = ['edge_dependency']
# # SG
# edge_properties = ['edge_codehash', 'edge_similar']
# # CG
edge_properties = ['edge_coexisting']

classify(input_folder,output_folder,edge_properties)