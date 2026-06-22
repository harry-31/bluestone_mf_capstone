import pandas as pd 
import os
folder_path = 'data/raw/'

csv_files = os.listdir(folder_path)

for file in csv_files:
    if file.endswith('.csv'):
        print("file name: ", file)

        file_path=folder_path +file
        df=pd.read_csv(file_path)

        print("\nShape:",df.shape)
        print("\nDatatypes:",df.dtypes)
        print("\nFirst 5 Records:",df.head())
        print("\nMissing Values:",df.isnull().sum())

