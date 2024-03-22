import pandas as pd
import networkx as nx
import json
from tqdm import tqdm
import ast


def handle_non_serializable(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, nx.classes.reportviews.NodeDataView):
        return list(obj)

def append_kg_to_json(graph, filename):
    json_data = nx.node_link_data(graph)
    json_str = json.dumps(json_data, indent=4, default=handle_non_serializable)
    with open(filename, 'a', encoding='utf-8') as json_file:
        json_file.write(json_str)
        json_file.write("\n") 

def bulid_kg(path,sheet_name,KG_path):
    # df = pd.read_csv(path)
    df = pd.read_excel(path,sheet_name=sheet_name)

    # bulid KG
    graph = nx.Graph()
    node_count = 0

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Building Knowledge Graph"):

        node_data = {
            "package_id": row['ID'],
            "OSS": row['OSS'],
            "Source": row['Source'],
            "Status": row['Status'],
            "filepath": row['SourcePath'],
            "package_name": row['name_version'],
            "sourcecode_hash": row['SourceCode_hash'],
            "dependency": row['dependency'],
            "source_publish": row['time'],
            "API_Use": row['code_api'],
            "Tokens_num": row['n_tokens'],
            "Embedding_vector": row['embedding'],
            "Cluster_type": row['Cluster'],
            "Report": row['report_num'],

            "edge_name": list(),
            "edge_codehash": list(),
            "edge_dependency": list(),
            "edge_similar": list(),
            "edge_coexisting": list(),
        }

        # Handle missing values by converting them to None
        for key, value in node_data.items():
            if pd.isna(value):
                node_data[key] = None

        # Add nodes to the graph
        graph.add_node(row['ID'], **node_data)
        node_count += 1

        # if node_count % 5 == 0:
        #     append_kg_to_json(graph, 'pypi_knowledge_graph.json')

        for other_index, other_row in df.iterrows():
            if index != other_index:
                if node_data["package_name"] == other_row['name_version']:
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.add_edge(other_row['ID'], row['ID'])

                    graph.nodes[row['ID']].setdefault('edge_name', []).append(other_row['ID'])
                    graph.nodes[other_row['ID']].setdefault('edge_name', []).append(row['ID'])

                if node_data["sourcecode_hash"] == other_row['SourceCode_hash']:
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.add_edge(other_row['ID'], row['ID'])

                    graph.nodes[row['ID']].setdefault('edge_codehash', []).append(other_row['ID'])
                    graph.nodes[other_row['ID']].setdefault('edge_codehash', []).append(row['ID'])

        for other_index, other_row in df.iterrows():
            if index != other_index:
                # Temporarily convert dependency from string to list for comparison
                dependency_list = ast.literal_eval(node_data['dependency']) if pd.notna(node_data['dependency']) else []

                # Connect nodes only if name_version is one of the elements in the dependency list
                if pd.notna(other_row['name_version']) and \
                    any(str(other_row['name_version']) in dep for dep in dependency_list):
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.nodes[row['ID']].setdefault('edge_dependency', []).append(other_row['ID'])

        for other_index, other_row in df.iterrows():
            if index != other_index:
                if node_data["Cluster_type"] == other_row['Cluster']:
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.add_edge(other_row['ID'], row['ID'])

                    graph.nodes[row['ID']].setdefault('edge_similar', []).append(other_row['ID'])
                    graph.nodes[other_row['ID']].setdefault('edge_similar', []).append(row['ID'])

        for other_index, other_row in df.iterrows():
            if index != other_index:
                if (node_data["Report"] == other_row['report_num']) or \
        ((node_data["filepath"] == other_row['SourcePath']) and 
        (("Backstabbers-Knife-Collection" not in node_data["filepath"] and "snyk.io" not in node_data["filepath"] and
        node_data["filepath"] != 'https://github.com/advisories' and node_data["filepath"] != 'https://socket.dev/npm/category/removed' and
        node_data["filepath"] != 'phylum' and node_data["filepath"] != 'https://tianwen.qianxin.com/blog/2023/07/07/pypi-2023Q2-part1/' and
        node_data["filepath"] != 'https://tianwen.qianxin.com/blog/2023/07/14/pypi-2023Q2-part2/'))):
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.add_edge(other_row['ID'], row['ID'])

                    graph.nodes[row['ID']].setdefault('edge_coexisting', []).append(other_row['ID'])
                    graph.nodes[other_row['ID']].setdefault('edge_coexisting', []).append(row['ID'])

    json_data = nx.node_link_data(graph)
    json_str = json.dumps(json_data, indent=4, default=handle_non_serializable)
    with open(KG_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)

    print(f"The knowledge graph contains {node_count} nodes.")

# ruby as example
bulid_kg('KG/Data/ruby_end.xlsx','KG','KG/KG/ruby_knowledge_graph_with_edges.json')


