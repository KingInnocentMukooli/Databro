"""
Demo script showing how to use the DataBro library.
"""
from databro.data_loader import DataLoader
from databro.data_preprocessor import DataPreprocessor
from databro.data_visualizer import DataVisualizer
from databro.data_summarizer import DataSummarizer

def main():
    # Initialize components
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    visualizer = DataVisualizer()
    summarizer = DataSummarizer()
    
    # Load data (replace with your CSV file path)
    print("Loading data...")
    df = loader.load_csv("your_data.csv")
    
    if df is None:
        return
        
    # Show basic information
    loader.get_info()
    loader.show_sample()
    
    # Handle missing values and scale data
    print("\nPreprocessing data...")
    df = preprocessor.handle_missing(df, strategy='mean')
    df = preprocessor.scale_data(df, method='standard')
    
    # Create visualizations
    print("\nCreating visualizations...")
    # Replace 'column_name' with actual column names from your data
    visualizer.plot_histogram(df, 'column_name', interactive=True)
    visualizer.plot_heatmap(df)
    
    # Generate and save summary
    print("\nGenerating summary...")
    summary = summarizer.get_basic_stats(df)
    summarizer.save_summary(summary, "summary.csv")
    
    # Generate comprehensive report
    summarizer.generate_report(df, "report.txt")

if __name__ == "__main__":
    main()
