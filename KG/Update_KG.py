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

def update_node_in_graph(graph, node_id, new_source_publish,new_SourcePath, new_Source,new_Status):
    if node_id not in graph.nodes:
        print(f"Node with ID {node_id} not found in the graph.")
        return

    graph.nodes[node_id]["source_publish"] = new_source_publish
    graph.nodes[node_id]["filepath"] = new_SourcePath
    graph.nodes[node_id]["Source"] = new_Source
    graph.nodes[node_id]["Status"] = new_Status


def update_node_from_excel(graph, excel_path, sheet_name):
    df_update = pd.read_excel(excel_path, sheet_name=sheet_name).applymap(lambda x: x.strip() if isinstance(x, str) else x)

    for index, row in tqdm(df_update.iterrows(), total=len(df_update), desc="Updating Knowledge Graph"):
        node_id = row['ID']
        new_source_publish = str(row['time'])
        new_SourcePath = row['SourcePath']
        new_Source = row['Source']
        new_Status = row['Status']

        new_source_publish = None if pd.isna(new_source_publish) or new_source_publish == '' else new_source_publish

        update_node_in_graph(graph, node_id, new_source_publish, new_SourcePath, new_Source,new_Status)


def update_kg(excel_path,sheet_name,KG_path):
    with open('KG/Data/npm_knowledge_graph_with_edges.json', 'r', encoding='utf-8') as json_file:
        graph_data = json.load(json_file)

    graph = nx.node_link_graph(graph_data)

    update_node_from_excel(graph, excel_path, sheet_name)

    updated_json_data = nx.node_link_data(graph)
    updated_json_str = json.dumps(updated_json_data, indent=4, default=handle_non_serializable)
    with open(KG_path, 'w', encoding='utf-8') as updated_json_file:
        updated_json_file.write(updated_json_str)

# ruby as example
update_kg('KG/Data/ruby_end.xlsx','KG','KG/KG/ruby_knowledge_graph_with_edges.json')