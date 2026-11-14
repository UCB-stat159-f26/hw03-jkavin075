# tennis_career

A Python package that analyzes Serena Williams's career match statistics and opponent age differentials. 

This package provides data pipelines to clean, process, and visualize historical tennis match data. More specifically, it recreates plots that were originally published by the New York Times. The package does this by using Python, Pandas, and Seaborn.

## Repository Structure

```text
├── tennis_career/          
│   ├── __init__.py
│   └── data.py             # Data loading and processing functions
├── tests/                  # Pytest suite for testing the package
│   ├── __init__.py
│   └── test_data.py        # Test cases
├── pyproject.toml          # Package configuration
└── README.md               # Documentation
```

## Installation

This package is hosted in the `hw03-jkavin075` repository. You can install it directly into your Python environment using `pip`. 

It is recommended to use an isolated environment (like Conda or venv) with Python 3.11+.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-organization]/hw03-jkavin075.git
   cd hw03-jkavin075
   ```

2. **Install the package:**
   To install the `tennis_career` package for standard use:
   ```bash
   pip install .
   ```
   *Note for developers: If you plan to modify the code, install it in editable mode instead using `pip install -e .`*

## Developer Reflection

Building this package yielded a few necessary lessons regarding reproducible open-source data science:

I learned how Python handles module paths, and why just having files in a directory is not enough. Using `pyproject.toml` to formally define the `tennis_career` package and using standard `pip` installations was very important for other users to run the package and reproduce the results. Also, working with and setting up Pytest helped me understand how relative and absolute imports work across different directories. I ensured that pytest interacted with the package how an end user would.

## Languages and Libraries Used

* **Python 3.11+**
* **Pandas:** For cleaning, merging, and aggregating career match records.
* **Seaborn & Matplotlib:** For rendering the final age differential distributions and scatter plots.
* **Pytest:** For module verification and continuous integration.