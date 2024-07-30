import pandas as pd
import os

def create_data(file_path: str, name: str, phone: str):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['Index', 'Ism', 'Raqam'])
        df.to_excel(file_path, index=False)
    else:

        df = pd.read_excel(file_path)

    new_index = len(df) + 1
    new_data = pd.DataFrame({'Index': [new_index], 'Ism': [name], 'Raqam': [phone]})
    df = pd.concat([df, new_data], ignore_index=True)
    
    df.to_excel(file_path, index=False)