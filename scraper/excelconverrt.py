import pandas as pd
import openpyxl
import random
import os
import subprocess


def convert(email_list, excel_file_name):
    emails = list()
    links = list()
    output_directory = "C:/ExcelFiles"  # Change this to your desired directory

    # Create the directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create the full path for the Excel file

    for i in email_list:
        emails.append(i[0])
        links.append(i[1])

    data = {"Email": emails, "Link": links}
    data_frame = pd.DataFrame(data)
    try:
        full_path = os.path.join(output_directory, f"{excel_file_name}.xlsx")
        if os.path.isfile(full_path):
            # full_path = os.path.join(output_directory, f"{excel_file_name}.xlsx")
            data_frame.to_excel(full_path)
            subprocess.run(["start", full_path], shell=True)
        else:
            randomlist = []
        for i in range(0,10):
            n = random.randint(1,9)
            randomlist.append(n)
        randomlist = ''.join(map(str, randomlist))
        full_path = os.path.join(output_directory, f"{excel_file_name}{randomlist}.xlsx")      
        data_frame.to_excel(full_path)
        subprocess.run(["start", full_path], shell=True)
    except: 
        randomlist = []
        for i in range(0,10):
            n = random.randint(1,9)
            randomlist.append(n)
        randomlist = ''.join(map(str, randomlist))
        full_path = os.path.join(output_directory, f"{excel_file_name}{randomlist}.xlsx")      
        data_frame.to_excel(full_path)
        subprocess.run(["start", full_path], shell=True)
    





