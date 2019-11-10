import pandas as pd
import openpyxl
import os

data_dir = "."
team_wkbk = "chartme_template.xlsx"

wb = openpyxl.load_workbook(os.path.join(data_dir, team_wkbk))
r = wb.get_named_range('data')
for ws in wb.worksheets:
    ws.activate
    a=1
b=2