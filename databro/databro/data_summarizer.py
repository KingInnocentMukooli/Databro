"""
DataBro Data Summarizer module for generating and exporting data summaries.
"""
import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Union
import json
from tabulate import tabulate

class DataSummarizer:
    """Class for summarizing data and generating reports."""
    
    def __init__(self):
        """Initialize DataSummarizer."""
        pass
        
    def get_basic_stats(self, 
                       df: pd.DataFrame,
                       columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Get basic statistical summary of numerical columns.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Specific columns to summarize
            
        Returns:
            pd.DataFrame: Statistical summary
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
            
        return df[columns].describe()
    
    def get_categorical_summary(self,
                              df: pd.DataFrame,
                              columns: Optional[List[str]] = None) -> Dict:
        """
        Get summary of categorical columns.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Specific categorical columns
            
        Returns:
            Dict: Dictionary containing value counts for each categorical column
        """
        if columns is None:
            columns = df.select_dtypes(include=['object']).columns
            
        summary = {}
        for col in columns:
            summary[col] = df[col].value_counts().to_dict()
            
        return summary
    
    def get_correlation_summary(self,
                              df: pd.DataFrame,
                              columns: Optional[List[str]] = None,
                              threshold: float = 0.5) -> pd.DataFrame:
        """
        Get correlation summary highlighting strong correlations.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Specific columns to analyze
            threshold (float): Correlation strength threshold
            
        Returns:
            pd.DataFrame: Strong correlations
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
            
        corr = df[columns].corr()
        strong_corr = corr[abs(corr) > threshold]
        return strong_corr
    
    def save_summary(self,
                    summary: Union[pd.DataFrame, Dict],
                    file_path: str,
                    format: str = 'csv') -> None:
        """
        Save summary to file.
        
        Args:
            summary: Summary to save
            file_path (str): Path to save the file
            format (str): Output format ('csv', 'json', or 'txt')
        """
        try:
            if format == 'csv':
                if isinstance(summary, pd.DataFrame):
                    summary.to_csv(file_path)
                else:
                    pd.DataFrame(summary).to_csv(file_path)
            elif format == 'json':
                if isinstance(summary, pd.DataFrame):
                    summary.to_json(file_path)
                else:
                    with open(file_path, 'w') as f:
                        json.dump(summary, f, indent=4)
            elif format == 'txt':
                with open(file_path, 'w') as f:
                    if isinstance(summary, pd.DataFrame):
                        f.write(tabulate(summary, headers='keys', tablefmt='grid'))
                    else:
                        f.write(str(summary))
            print(f"Summary saved to {file_path}")
        except Exception as e:
            print(f"Error saving summary: {str(e)}")
    
    def generate_report(self,
                       df: pd.DataFrame,
                       file_path: str,
                       include_categorical: bool = True) -> None:
        """
        Generate a comprehensive report including all summaries.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            file_path (str): Path to save the report
            include_categorical (bool): Whether to include categorical summaries
        """
        with open(file_path, 'w') as f:
            # Basic information
            f.write("=== Dataset Overview ===\n")
            f.write(f"Number of rows: {len(df)}\n")
            f.write(f"Number of columns: {len(df.columns)}\n\n")
            
            # Numerical summary
            f.write("=== Numerical Summary ===\n")
            f.write(tabulate(self.get_basic_stats(df), headers='keys', tablefmt='grid'))
            f.write("\n\n")
            
            # Categorical summary if requested
            if include_categorical:
                f.write("=== Categorical Summary ===\n")
                cat_summary = self.get_categorical_summary(df)
                for col, counts in cat_summary.items():
                    f.write(f"\n{col}:\n")
                    f.write(tabulate(pd.DataFrame(counts.items(), 
                                                columns=['Value', 'Count']),
                                   headers='keys',
                                   tablefmt='grid'))
                f.write("\n\n")
            
            # Correlation summary
            f.write("=== Strong Correlations ===\n")
            f.write(tabulate(self.get_correlation_summary(df),
                           headers='keys',
                           tablefmt='grid'))
            
        print(f"Report generated and saved to {file_path}")
