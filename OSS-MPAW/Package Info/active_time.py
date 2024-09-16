import os
import json
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import pandas as pd

def extract_nodes(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if 'nodes' in data:
            return data['nodes']
        else:
            return []

def parse_date(date_str):
    try:
        # Try parsing the date with ISO 8601 format
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        try:
            # Try parsing the date with month/day/year format
            return datetime.strptime(date_str, '%m/%d/%y')
        except ValueError:
            # Try parsing the date with other formats using dateutil.parser
            return date_parser.parse(date_str)

def sort_nodes_by_published_at(nodes):
    return sorted(nodes, key=lambda node: parse_date(node.get('published_at')))

def process_folder(folder_path):
    total_df = pd.DataFrame(columns=['File', 'Time_Interval_Minutes'])
   
    for json_file in os.listdir(folder_path):
        if json_file.endswith('.json'):
            json_path = os.path.join(folder_path, json_file)
            with open(json_path, "r", encoding="utf-8") as file:
                knowledge_graph = json.load(file)

            nodes = extract_nodes(json_path)
            sorted_nodes = sort_nodes_by_published_at(nodes)
            
            # Calculate the time interval between the first and last nodes
            if sorted_nodes:
                first_node_timestamp = parse_date(sorted_nodes[0].get('published_at'))
                last_node_timestamp = parse_date(sorted_nodes[-1].get('published_at'))
                time_interval_minutes = round((last_node_timestamp - first_node_timestamp).total_seconds() / 60, 2)
                if time_interval_minutes == 0.0:
                    print(json_path)
            else:
                time_interval_minutes = 0
                print(json_path)

            # save to KG
            knowledge_graph["Active_Time"] = time_interval_minutes
            with open(json_path, "w", encoding="utf-8") as file:
                json.dump(knowledge_graph, file, ensure_ascii=False, indent=4)

# Specify the folder path to traverse
folder_path = ''
process_folder(folder_path)

