# get_overall_MR
import json

def process_json(json_data):
    sources_count = {}
    
    for node in json_data.get("nodes", []):
        status = node.get("Status", "")
        source = node.get("Source", "")
        edge_names = node.get("edge_name", [])

        # if the status of the node is untracked and there is a edge name
        if status == "untracked" and edge_names:
            for edge_name in edge_names:
                # obtain the status of the edge name point
                edge_node_status = get_edge_node_status(json_data, edge_name)
                # if at least one of the points has a tracked status the source count is incremented
                if edge_node_status == "tracked":
                    sources_count[source] = sources_count.get(source, 0) + 1
                    break

    return sources_count

def get_edge_node_status(json_data, edge_name):
    for node in json_data.get("nodes", []):
        if node.get("id") == edge_name:
            return node.get("Status", "")
    return ""

# read multiple json files
file_paths = [
    "KG/Duplicated_Edge/duplicate/npm_graph_name.json",
    "KG/Duplicated_Edge/duplicate/pypi_graph_name.json",
    "KG/Duplicated_Edge/duplicate/ruby_graph_name.json"

    # more...
]

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    result = process_json(json_data)
    print(f"Results for {file_path}:")
    for source, count in result.items():
        print(f"{source}: {count}")
    print("\n")
