# the sales data dataframes of each year will be merged
import pandas as pd
import os

path = r"C:\Users\Pablo\Documents\Data_Science_Folder\Portfolio_Projects\Sales_Analysis\Sales_Data"

all_files = [file for file in os.listdir(path= path) if file.endswith("csv")]
dataframes = []


for file in all_files:
    file_path = os.path.join(path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

all_sales = pd.concat(dataframes, ignore_index=True)
print(all_sales)

all_sales.to_csv(r"C:\Users\Pablo\Documents\Data_Science_Folder\Portfolio_Projects\Sales_Analysis\Sales_Data\all_sales.csv", index= False)