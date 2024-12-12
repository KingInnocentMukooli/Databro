from setuptools import setup, find_packages

setup(
    name="databro",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'numpy>=1.24.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'plotly>=5.13.0',
        'scikit-learn>=1.2.0',
        'tabulate>=0.9.0'
    ],
    author="Your Name",
    description="A comprehensive data science library for analysis and visualization",
    python_requires='>=3.8'
)
