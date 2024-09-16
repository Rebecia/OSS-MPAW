import os
import json
import requests
import time
from retry import retry
from requests.exceptions import RequestException
from tqdm import tqdm
import pandas as pd
import re

def is_valid_version(version):
    pattern = r'^\d+\.\d+(\.\d+)?(-[\w\d]+(\.[\w\d]+)*)?$'
    return re.match(pattern, version) is not None

@retry(tries=3, delay=2, backoff=2)
def fetch_package_info(processed_package_name, version):
    request_url = f'https://libraries.io/api/NPM/{processed_package_name}?api_key=xxxxxx'
    print(request_url)
    response = requests.get(request_url)
    response.raise_for_status()
    return response.json()

def process_excel_file(input_excel_path, output_excel_path):
    
    df = pd.read_excel(input_excel_path, sheet_name='Sheet1')
    
    
    package_names = df['name_version'].tolist()
    statuses = df['Status'].tolist()
    versionss =  df['version'].tolist()
    published_ats = df['published_at'].tolist()
    
    for index, package_name in enumerate(tqdm(package_names, desc="Processing packages")):
        Status = statuses[index]
        published_at = published_ats[index]
        if Status == 'untracked' and pd.isna(published_at):
            if '-' in package_name:
                package_name_parts = package_name.split('-')
                version = package_name_parts[-1]
                if is_valid_version(version):
                    if version.startswith('v'):
                        version = version[1:]
                    package_name = '-'.join(package_name_parts[:-1])
                else:
                    package_name = '-'.join(package_name_parts)
                    version = None
            else:
                version = None

            if version != None:
                df.at[index, 'version'] = version
                print(version)
            
                processed_package_name = '%2F'.join(package_name.split('/'))

                try:
                    response_data = fetch_package_info(processed_package_name, version)
                except RequestException as e:
                    print("Request Error occurred:", e)
                    time.sleep(5)  
                    continue

                versions = response_data.get('versions', [])
                published_at = 'Not available'
                for version_info in versions:
                    if version_info['number'] == version:
                        published_at = version_info.get('published_at', 'Not available')
                        print(published_at)
                        break
                
                
                df.at[index, 'published_at'] = published_at

                
                time.sleep(1 / 60)

    
    df.to_excel(output_excel_path, index=False)

input_excel_path = ''  
output_excel_path = ''  

process_excel_file(input_excel_path, output_excel_path)