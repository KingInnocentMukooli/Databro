# DataBro

[![Python Package](https://github.com/KingInnocentMukooli/Databro/actions/workflows/python-package.yml/badge.svg)](https://github.com/KingInnocentMukooli/Databro/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/databro.svg)](https://badge.fury.io/py/databro)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive data science library for streamlined data preprocessing and visualization.

## Features

### Data Loading
- Easy CSV file loading
- Automatic data type detection
- Missing value analysis
- Dataset information summary

### Data Preprocessing
- Missing value handling (mean, median, mode, drop)
- Data scaling (standard, min-max)
- Categorical encoding
- Outlier removal (IQR, z-score)

### Data Visualization
- Histograms
- Scatter plots
- Correlation heatmaps
- Box plots
- Interactive visualizations

### Data Summarization
- Statistical summaries
- Categorical analysis
- Correlation analysis
- Multi-format export (CSV, JSON, TXT)
- Comprehensive reporting

## Installation

```bash
pip install databro
```

## Quick Start

```python
from databro import DataLoader, DataPreprocessor, DataVisualizer, DataSummarizer

# Initialize components
loader = DataLoader()
preprocessor = DataPreprocessor()
visualizer = DataVisualizer()
summarizer = DataSummarizer()

# Load and analyze data
df = loader.load_csv("your_data.csv")
info = loader.get_info(df)
print(info)

# Preprocess data
df_processed = preprocessor.handle_missing(df, method='mean')
df_scaled = preprocessor.scale_data(df_processed, method='standard')

# Create visualizations
visualizer.plot_histogram(df, "column_name")
visualizer.plot_heatmap(df)

# Get summary statistics
summary = summarizer.get_basic_stats(df)
print(summary)
```

## Documentation

For detailed documentation, visit our [GitHub Wiki](https://github.com/KingInnocentMukooli/Databro/wiki).

### Example Notebooks
- [Basic Usage Demo](examples/databro_demo.ipynb)
- [Multiple Datasets Analysis](examples/multiple_datasets_demo.ipynb)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Mukooli Innocent**
- Email: mukooliinnocent@gmail.com
- GitHub: [@KingInnocentMukooli](https://github.com/KingInnocentMukooli)

## Show your support

Give a ⭐️ if this project helped you!

## Citation

If you use DataBro in your research, please cite:

```bibtex
@software{databro2024mukooli,
  author = {Mukooli, Innocent},
  title = {DataBro: A Comprehensive Data Science Library},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/KingInnocentMukooli/Databro}
}
```

## Requirements

- Python >=3.8
- pandas >=2.0.0
- numpy >=1.24.0
- matplotlib >=3.7.0
- seaborn >=0.12.0
- plotly >=5.13.0
- scikit-learn >=1.2.0
- tabulate >=0.9.0

## Project Links

- GitHub: [https://github.com/KingInnocentMukooli/Databro](https://github.com/KingInnocentMukooli/Databro)
- PyPI: [https://pypi.org/project/databro/](https://pypi.org/project/databro/)
