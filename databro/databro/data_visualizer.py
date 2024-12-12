"""
DataBro Data Visualizer module for creating various plots and visualizations.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from typing import Optional, List, Union

class DataVisualizer:
    """Class for creating data visualizations."""
    
    def __init__(self):
        """Initialize DataVisualizer."""
        self.style = 'seaborn'
        plt.style.use(self.style)
        
    def plot_histogram(self,
                      df: pd.DataFrame,
                      column: str,
                      bins: int = 30,
                      interactive: bool = False) -> None:
        """
        Create a histogram for a numerical column.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            column (str): Column to plot
            bins (int): Number of bins
            interactive (bool): Whether to use plotly for interactive plot
        """
        if interactive:
            fig = px.histogram(df, x=column, nbins=bins)
            fig.show()
        else:
            plt.figure(figsize=(10, 6))
            sns.histplot(data=df, x=column, bins=bins)
            plt.title(f'Distribution of {column}')
            plt.show()
    
    def plot_scatter(self,
                    df: pd.DataFrame,
                    x: str,
                    y: str,
                    hue: Optional[str] = None,
                    interactive: bool = False) -> None:
        """
        Create a scatter plot.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            x (str): Column for x-axis
            y (str): Column for y-axis
            hue (str, optional): Column for color coding points
            interactive (bool): Whether to use plotly for interactive plot
        """
        if interactive:
            fig = px.scatter(df, x=x, y=y, color=hue)
            fig.show()
        else:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x=x, y=y, hue=hue)
            plt.title(f'{y} vs {x}')
            plt.show()
    
    def plot_heatmap(self,
                    df: pd.DataFrame,
                    columns: Optional[List[str]] = None) -> None:
        """
        Create a correlation heatmap.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            columns (List[str], optional): Specific columns to include
        """
        if columns is not None:
            correlation = df[columns].corr()
        else:
            correlation = df.select_dtypes(include=[np.number]).corr()
            
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Heatmap')
        plt.show()
    
    def plot_box(self,
                df: pd.DataFrame,
                column: str,
                by: Optional[str] = None,
                interactive: bool = False) -> None:
        """
        Create a box plot.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            column (str): Column to plot
            by (str, optional): Column to group by
            interactive (bool): Whether to use plotly for interactive plot
        """
        if interactive:
            fig = px.box(df, y=column, x=by)
            fig.show()
        else:
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df, y=column, x=by)
            plt.title(f'Box Plot of {column}')
            plt.show()
    
    def plot_count(self,
                  df: pd.DataFrame,
                  column: str,
                  interactive: bool = False) -> None:
        """
        Create a count plot for categorical data.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            column (str): Column to plot
            interactive (bool): Whether to use plotly for interactive plot
        """
        if interactive:
            fig = px.bar(df[column].value_counts().reset_index(),
                        x='index', y=column)
            fig.show()
        else:
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=column)
            plt.title(f'Count Plot of {column}')
            plt.xticks(rotation=45)
            plt.show()
