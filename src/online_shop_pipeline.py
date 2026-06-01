from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np

def fetch_data():
    online_shoppers_purchasing_intention_dataset = fetch_ucirepo(id=468) 
    X = online_shoppers_purchasing_intention_dataset.data.features 
    y = online_shoppers_purchasing_intention_dataset.data.targets 
    df = pd.concat([X,y], axis=1)
    return df  

def clean_data(df):
    df_cleaned = df.copy()
    df_cleaned['ProductRelated_Duration'] = np.where(df_cleaned['ProductRelated_Duration'] > 3600, 3600, df_cleaned['ProductRelated_Duration'])
    df_cleaned['Administrative_Duration'] = np.where(df_cleaned['Administrative_Duration'] > 3600, 3600, df_cleaned['Administrative_Duration'])
    df_cleaned['Informational_Duration'] = np.where(df_cleaned['Informational_Duration'] > 3600, 3600, df_cleaned['Informational_Duration'])
    df_cleaned['Weekend'] = df_cleaned['Weekend'].astype(int)
    df_cleaned['Revenue'] = df_cleaned['Revenue'].astype(int)
    df_cleaned = pd.get_dummies(df_cleaned, columns=['Month', 'VisitorType'], drop_first=True)
    return df_cleaned

def save_data(df, filepath):
    df.to_csv(filepath,index=False)