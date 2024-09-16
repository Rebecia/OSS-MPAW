import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def find_urls(name, html_content):
    result_urls = []

    # Check if name is in the HTML content
    if name in html_content:
        result_urls.append(html_content)

    return result_urls

def get_report_fromURL(excel1_path,excel1_sheet_name,excel1_output_excel_path):
    df1 = pd.read_excel(excel1_path, sheet_name=excel1_sheet_name)

    # Read report file
    excel2_path = 'Get_KG_Need/get_report/report.xlsx'
    excel2_sheet_name = 'url'  
    df2 = pd.read_excel(excel2_path, sheet_name=excel2_sheet_name)

    # Define counter
    counter = 0

    # Iterate over URLs in Excel2
    for _, row in tqdm(df2.iterrows(), total=len(df2), desc="Processing URLs"):
        url = row['URL']

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if request was successful
            html_content = response.text

            # Iterate over 'name_version' in Excel1
            for index, row in tqdm(df1.iterrows(), total=len(df1), desc="Processing Excel1"):
                name = row['name_version']

                # Get matching URLs for each 'name_version'
                result_urls = find_urls(name, html_content)
                
                # Append URL to the fifth column of the corresponding row in Excel1
                if result_urls:
                    temp = []
                    if (index, 'report_num') in df1.index:
                        temp = df1[index, 'report_num']
                    temp.append(url)
                    df1.at[index, 'report_num'] = temp

            counter += 1

            # Save Excel1 every 5 URL processed
            if counter == 5:
                df1.to_csv(excel1_output_excel_path, index=False)
                counter = 0  # Reset counter

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching URL {url}: {e}")

        # Finally, save the updated Excel1
        df1.to_csv(excel1_output_excel_path, index=False)
