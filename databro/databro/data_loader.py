"""
DataBro Data Loader module for handling data import and basic inspection.
"""
import pandas as pd
from typing import Union, List, Optional
import os

class DataLoader:
    """Class for loading and inspecting data."""
    
    def __init__(self):
        """Initialize DataLoader."""
        self.current_data = None
        
    def load_csv(self, file_path: str, encoding: str = 'utf-8', **kwargs) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.
        
        Args:
            file_path (str): Path to the CSV file
            encoding (str): File encoding (default: 'utf-8')
            **kwargs: Additional arguments to pass to pd.read_csv
            
        Returns:
            pd.DataFrame: Loaded data
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
                
            self.current_data = pd.read_csv(file_path, encoding=encoding, **kwargs)
            return self.current_data
            
        except Exception as e:
            print(f"Error loading file: {str(e)}")
            return None
    
    def show_sample(self, n: int = 5) -> None:
        """
        Display the first n rows of the dataset.
        
        Args:
            n (int): Number of rows to display (default: 5)
        """
        if self.current_data is None:
            print("No data loaded. Please load data first using load_csv().")
            return
            
        print("\nFirst", n, "rows of the dataset:")
        print(self.current_data.head(n))
    
    def get_info(self) -> None:
        """Display information about the dataset."""
        if self.current_data is None:
            print("No data loaded. Please load data first using load_csv().")
            return
            
        print("\nDataset Info:")
        print(f"Number of rows: {len(self.current_data)}")
        print(f"Number of columns: {len(self.current_data.columns)}")
        print("\nColumn Details:")
        print(self.current_data.info())
        
    def get_column_types(self) -> dict:
        """
        Get the data types of all columns.
        
        Returns:
            dict: Dictionary of column names and their data types
        """
        if self.current_data is None:
            print("No data loaded. Please load data first using load_csv().")
            return {}
            
        return dict(self.current_data.dtypes)
    
    def get_missing_info(self) -> pd.Series:
        """
        Get information about missing values in each column.
        
        Returns:
            pd.Series: Series containing the count of missing values per column
        """
        if self.current_data is None:
            print("No data loaded. Please load data first using load_csv().")
            return pd.Series()
            
        return self.current_data.isnull().sum()
