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

def bulid_kg():

    excel_path = 'Data collection/malware/malware.xlsx'  
    sheet_name = 'RubyGems'        
    # df = pd.read_csv(excel_path)
    df = pd.read_excel(excel_path,sheet_name=sheet_name)

    graph = nx.Graph()
    node_count = 0

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Building Knowledge Graph"):
        node_data = {
            "package_id": row['ID'],
            "OSS": row['OSS'],
            "Source": row['Source'],
            "Status": row['Status'],
            "package_name": row['name_version'],

            "edge_name": list(),

        }

        for key, value in node_data.items():
            if pd.isna(value):
                node_data[key] = None
        graph.add_node(row['ID'], **node_data)
        node_count += 1


        for other_index, other_row in df.iterrows():
            if index != other_index:
                if node_data["package_name"] == other_row['name_version']:
                    graph.add_edge(row['ID'], other_row['ID'])
                    graph.add_edge(other_row['ID'], row['ID'])

                    graph.nodes[row['ID']].setdefault('edge_name', []).append(other_row['ID'])
                    graph.nodes[other_row['ID']].setdefault('edge_name', []).append(row['ID'])

    # save as json
    json_data = nx.node_link_data(graph)
    json_str = json.dumps(json_data, indent=4, default=handle_non_serializable)
    with open('./ruby_graph_name.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)

    print(f"Knowledge Graph Included {node_count} nodes")


bulid_kg()
