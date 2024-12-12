"""
DataBro Data Preprocessor module for data cleaning and transformation.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from typing import Union, List, Optional

class DataPreprocessor:
    """Class for preprocessing data."""
    
    def __init__(self):
        """Initialize DataPreprocessor."""
        self.scaler = None
        
    def handle_missing(self, 
                      df: pd.DataFrame, 
                      strategy: str = 'mean',
                      columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Handle missing values in the dataset.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            strategy (str): Strategy to handle missing values ('mean', 'median', 'mode', 'drop')
            columns (List[str], optional): Specific columns to handle missing values
            
        Returns:
            pd.DataFrame: DataFrame with handled missing values
        """
        df_copy = df.copy()
        
        if columns is None:
            columns = df.columns
            
        for col in columns:
            if df_copy[col].isnull().any():
                if strategy == 'mean':
                    df_copy[col].fillna(df_copy[col].mean(), inplace=True)
                elif strategy == 'median':
                    df_copy[col].fillna(df_copy[col].median(), inplace=True)
                elif strategy == 'mode':
                    df_copy[col].fillna(df_copy[col].mode()[0], inplace=True)
                elif strategy == 'drop':
                    df_copy.dropna(subset=[col], inplace=True)
                    
        return df_copy
    
    def scale_data(self, 
                   df: pd.DataFrame,
                   method: str = 'standard',
                   columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Scale numerical data.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            method (str): Scaling method ('standard' or 'minmax')
            columns (List[str], optional): Specific columns to scale
            
        Returns:
            pd.DataFrame: Scaled DataFrame
        """
        df_copy = df.copy()
        
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
            
        if method == 'standard':
            self.scaler = StandardScaler()
        else:
            self.scaler = MinMaxScaler()
            
        df_copy[columns] = self.scaler.fit_transform(df_copy[columns])
        return df_copy
    
    def encode_categorical(self,
                         df: pd.DataFrame,
                         columns: Optional[List[str]] = None,
                         method: str = 'onehot') -> pd.DataFrame:
        """
        Encode categorical variables.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Columns to encode
            method (str): Encoding method ('onehot' or 'label')
            
        Returns:
            pd.DataFrame: DataFrame with encoded categories
        """
        df_copy = df.copy()
        
        if columns is None:
            columns = df.select_dtypes(include=['object']).columns
            
        if method == 'onehot':
            return pd.get_dummies(df_copy, columns=columns)
        else:
            for col in columns:
                df_copy[col] = pd.Categorical(df_copy[col]).codes
            return df_copy
    
    def remove_outliers(self,
                       df: pd.DataFrame,
                       columns: Optional[List[str]] = None,
                       method: str = 'iqr',
                       threshold: float = 1.5) -> pd.DataFrame:
        """
        Remove outliers from the dataset.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Columns to check for outliers
            method (str): Method to detect outliers ('iqr' or 'zscore')
            threshold (float): Threshold for outlier detection
            
        Returns:
            pd.DataFrame: DataFrame with outliers removed
        """
        df_copy = df.copy()
        
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
            
        for col in columns:
            if method == 'iqr':
                Q1 = df_copy[col].quantile(0.25)
                Q3 = df_copy[col].quantile(0.75)
                IQR = Q3 - Q1
                df_copy = df_copy[~((df_copy[col] < (Q1 - threshold * IQR)) | 
                                  (df_copy[col] > (Q3 + threshold * IQR)))]
            else:  # zscore
                z_scores = np.abs((df_copy[col] - df_copy[col].mean()) / df_copy[col].std())
                df_copy = df_copy[z_scores < threshold]
                
        return df_copy
