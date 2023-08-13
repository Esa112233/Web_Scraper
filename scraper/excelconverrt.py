import pandas as pd
import openpyxl


def convert(email_list):
    for i in email_list:

        data = pd.DataFrame([i[0], i[1]],
                        columns=['Emails', 'Links'])
    data.to_excel("hello1.xlsx")