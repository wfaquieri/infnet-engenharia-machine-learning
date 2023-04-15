"""
This code contains a pipeline for data preparation, called 'PreparacaoDados', generated using Kedro 0.18.7.

The pipeline consists of three functions:
- load_data(): loads a CSV file located in '../data/01_raw/data.csv' and selects a subset of columns;
- filter_data(df): filters the dataframe to include only rows where 'shot_type' equals '2PT Field Goal' and drops any rows with missing values;
- split_data(df, test_size=0.2, random_state=42): splits the dataframe into training and testing sets using stratified sampling and returns four dataframes: X_train, X_test, y_train, and y_test.

The split_data() function accepts three parameters:
- df (pd.DataFrame): The dataframe to split.
- test_size (float): The proportion of the data to use for testing (default = 0.2).
- random_state (int): The random seed to use for the split (default = 42).

It returns four dataframes:
- X_train (pd.DataFrame): The features of the training set.
- X_test (pd.DataFrame): The features of the testing set.
- y_train (pd.Series): The target values of the training set.
- y_test (pd.Series): The target values of the testing set.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from kedro_mlflow.io.metrics import MlflowMetricDataSet

def select_data(data: pd.DataFrame):
    data = data[['lat','lon','minutes_remaining','period','playoffs','shot_distance','shot_type','shot_made_flag']]
    return data

def filter_data(data: pd.DataFrame, shot_type_filter):
    df_filtrado = data[data['shot_type'] == shot_type_filter]
    df_filtrado = df_filtrado.dropna()
    return df_filtrado

def split_data(data: pd.DataFrame, test_size, random_state):

    X = data.drop('shot_made_flag', axis=1)  
    y = data['shot_made_flag'] 

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def split_metrics(X_train, X_test, test_size):
    metrics = {
        'train_df_size': X_train.shape[0],
        'test_df_size': X_test.shape[0],
        'test_size_perc': test_size
    }

    return {
        key: {'value': float(value) if isinstance(value, (int, float)) else value, 'step': 1}
        for key, value in metrics.items()
    }

    

