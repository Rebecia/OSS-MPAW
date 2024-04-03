import os
import json
from datetime import datetime
from dateutil import parser as date_parser
import pandas as pd
import re

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
    return sorted(nodes, key=lambda node: parse_date(node.get('published_at', node.get('source_publish', ''))))

def count_lines(file_path):
    if file_path is None or not os.path.isfile(file_path):  #
        return 0
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

def process_folders(folder_paths,excel_path):
    import os
    import json
    import pandas as pd
    
    # Initialize an empty DataFrame
    total_df = pd.DataFrame(columns=['File','Sort_ID','Active Time','Ave Download Number','Download Number','evolution','Ave Report Number','Report Number'])
    
    for folder_path in folder_paths:
        for json_file in os.listdir(folder_path):
            if json_file.endswith('.json'):
                json_path = os.path.join(folder_path, json_file)

                # Read JSON file
                with open(json_path, "r", encoding="utf-8") as file:
                    knowledge_graph = json.load(file)

                # Extract required fields
                Active_Time = knowledge_graph["Active_Time"]
                Ave_Download_Number = knowledge_graph["Ave_dowanload_num"]
                Ave_Report_Number = knowledge_graph["Ave_report_num"]

                nodes = extract_nodes(json_path)
                sorted_nodes = sort_nodes_by_published_at(nodes)

                # Initialize variables
                dependency_num = 0
                description_num = 0
                name_num = 0
                hash_num = 0
                version_num = 0
                line_difference = []
                evolutions = ''
                sort_node = ''
                sort_download_num = ''
                sort_report_num = ''
                previous_node = None
                
                for node in sorted_nodes:
                    # Process each node
                    id_node = node.get('id', '')
                    sort_node += str(id_node) + ', '

                    if 'download_number' in node:
                        temp_download_num = node.get('download_number', '')
                        sort_download_num += str(temp_download_num) + ', '
                    else:
                        sort_download_num += 'Null , '

                    if 'report_num' in node:
                        temp_report_num = node.get('report_num', '')
                        sort_report_num += str(temp_report_num) + ', '
                    else:
                        sort_report_num += 'Null, '

                    if previous_node:
                        if node.get('dependency', '') != previous_node.get('dependency', ''):
                            dependency_num += 1
                            evolutions += 'dependency_change, '

                        if node.get('description', '') != previous_node.get('description', ''):
                            description_num += 1
                            evolutions += 'description_change, '

                        package_name_split = node.get('package_name', '').split('-')
                        if re.match(r'^\d+(\.\d+)?$', package_name_split[-1]):
                            package_name1 = '-'.join(package_name_split[:-1])
                        else:
                            package_name1 = node.get('package_name', '')

                        package_name_split = previous_node.get('package_name', '').split('-')
                        if re.match(r'^\d+(\.\d+)?$', package_name_split[-1]):
                            package_name2 = '-'.join(package_name_split[:-1])
                        else:
                            package_name2 = previous_node.get('package_name', '')                    

                        if package_name1 != package_name2:
                            name_num += 1
                            evolutions += 'name_change, '
                        else:
                            print(json_file,package_name1,)
                            print(package_name2)

                        if node.get('sourcecode_hash', '') != previous_node.get('sourcecode_hash', ''):
                            hash_num += 1

                            code_path1 = node.get('SourceCode')
                            code_path2 = previous_node.get('SourceCode')
                            LoC1 = 0
                            LoC2 = 0
                            if code_path1 is not None:
                                LoC1 = count_lines(code_path1) 
                            if code_path2 is not None:
                                LoC2 = count_lines(code_path2)                         

                            line_difference.append(LoC2- LoC1)
                            evolutions += 'code_change and line changes ' + str(LoC2- LoC1) + ' lines, '
                        if package_name1 == package_name2 and node.get('version', '') != previous_node.get('version', ''):
                            version_num += 1
                            evolutions += 'version_change, '

                        evolutions += '; '

                    previous_node = node

                # Prepare data for DataFrame
                data = {'File': [json_file], 'Sort_ID': [sort_node], 'Active Time(min)': [Active_Time], 
                        'Ave Download Number': [Ave_Download_Number], 'Download Number': [sort_download_num], 
                        'evolution': [evolutions], 'Ave Report Number': [Ave_Report_Number], 
                        'Report Number': [sort_report_num]}

                # Create DataFrame for current folder and concatenate with total_df
                df = pd.DataFrame(data)
                total_df = pd.concat([total_df, df], ignore_index=True)

    # Write DataFrame to Excel
    total_df.to_excel(excel_path, index=False)

# Specify the folder path to traverse
folder_path = ['','',...]
excel_path = ''
process_folders(folder_path,excel_path)
