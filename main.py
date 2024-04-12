# Reading specific columns from an Excel File in Pandas 

import pandas as pd

file_path = 'example.xlsx'

df = pd.read_excel(
    file_path,
    usecols="A,D,E",
    engine='openpyxl'
)

print(df)
