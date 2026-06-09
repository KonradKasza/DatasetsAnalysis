from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np

def fetch_data():
    dataset = fetch_ucirepo(id=235) 
    df = dataset.data.features
    return df  

def clean_and_resample_data(df):
    df_cleaned = df.copy()
    continuous_features = [
        'Global_active_power', 'Global_reactive_power', 'Voltage', 
        'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'
    ]
    for col in continuous_features:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
    df_cleaned['Datetime'] = pd.to_datetime(df_cleaned['Date'] + ' ' + df_cleaned['Time'], dayfirst=True)
    df_cleaned = df_cleaned.set_index('Datetime')
    df_cleaned = df_cleaned.drop(columns=['Date', 'Time'])
    df_cleaned = df_cleaned.dropna()
    df_resampled = df_cleaned.resample('H').mean()
    df_resampled = df_resampled.dropna()  # ← FIX: usunięcie NaN po resampligu

    df_resampled['Hour'] = df_resampled.index.hour
    df_resampled['Day_of_week'] = df_resampled.index.dayofweek
    df_resampled['Is_Weekend'] = df_resampled.index.dayofweek.isin([5, 6]).astype(int)

    return df_resampled

def save_data(df, filepath):
    df.to_csv(filepath, index=True)