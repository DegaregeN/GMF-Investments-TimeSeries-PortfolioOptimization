
# GMF-Investments-TimeSeries-PortfolioOptimization

This project provides a comprehensive approach to financial data analysis, forecasting, and portfolio optimization for GMF Investments. It includes exploratory data analysis (EDA), time series forecasting with ARIMA, SARIMA, and LSTM models, and portfolio optimization based on forecast insights.

## Project Structure
The following layout describes each directory and its purpose in the project.

'''bash
GMF-Investments-TimeSeries-PortfolioOptimization/
│
├── README.md                        # Project overview, objectives, and usage instructions.
├── data/
│   ├── raw/                         # Raw data from YFinance, unprocessed.
│   ├── processed/                   # Cleaned and preprocessed data for modeling.
│   ├── README.md                    # Information on the datasets (TSLA, BND, SPY).
│   └── data_extraction.py           # Script to fetch data from YFinance.
│
├── notebooks/
│   ├── 01_data_exploration.ipynb    # EDA and preprocessing steps.
│   ├── 02_forecasting_models.ipynb  # Model building for time series forecasting.
│   ├── 03_forecast_analysis.ipynb   # Forecasting analysis and trend insights.
│   ├── 04_portfolio_optimization.ipynb # Portfolio optimization based on forecast.
│   └── helper_functions.py          # Common functions used across notebooks.
│
├── scripts/
│   ├── data_preprocessing.py        # Data cleaning, handling missing values, scaling.
│   ├── eda.py                       # Script for exploratory data analysis.
│   ├── forecasting_model.py         # Model selection and forecasting script (ARIMA, SARIMA, LSTM).
│   ├── forecast_analysis.py         # Analysis of forecast results.
│   ├── portfolio_optimization.py    # Portfolio optimization calculations.
│   └── utils.py                     # Utility functions for loading, plotting, etc.
│
├── models/
│   ├── trained_model_arima.pkl      # Trained ARIMA model for future use.
│   ├── trained_model_sarima.pkl     # Trained SARIMA model for future use.
│   ├── trained_model_lstm.h5        # Trained LSTM model for future use.
│   └── model_selection_notes.md     # Notes on model choice and parameters.
│
├── results/
│   ├── eda_visualizations/          # EDA plots (closing prices, volatility, outliers).
│   ├── forecast_visualizations/     # Forecast plots and trend visualizations.
│   ├── portfolio_performance/       # Portfolio performance metrics, risk-return analysis.
│   └── analysis_report.md           # Summary of insights and results.
│
├── requirements.txt                 # List of dependencies and packages.
└── references/
    ├── time_series_forecasting.md   # Links and notes on time series methods.
    ├── portfolio_optimization.md    # Links and notes on portfolio optimization techniques.
    └── literature/                  # Journal articles, papers, and reference documents.
'''bash


### Directory and File Descriptions

- **README.md**: Provides a high-level overview of the project, its objectives, and instructions for setup and usage.
  
- **data/**: Contains raw and processed data along with the `data_extraction.py` script to fetch financial data using the YFinance API.
  - `raw/`: Stores raw unprocessed data.
  - `processed/`: Holds cleaned and preprocessed data for modeling.
  - `README.md`: Describes the dataset details, including the three main assets (TSLA, BND, SPY).

- **notebooks/**: Jupyter notebooks for various stages of the project workflow.
  - `01_data_exploration.ipynb`: Initial EDA and data cleaning steps.
  - `02_forecasting_models.ipynb`: Time series forecasting model development.
  - `03_forecast_analysis.ipynb`: Analyzes forecast results and extracts insights.
  - `04_portfolio_optimization.ipynb`: Performs portfolio optimization using forecast results.
  - `helper_functions.py`: Contains reusable functions for notebook tasks.

- **scripts/**: Python scripts for data preprocessing, analysis, and forecasting.
  - `data_preprocessing.py`: Handles data cleaning, imputation, and scaling.
  - `eda.py`: Script for conducting EDA, including visualization of trends and volatility.
  - `forecasting_model.py`: Builds ARIMA, SARIMA, and LSTM models for time series forecasting.
  - `forecast_analysis.py`: Provides analysis of forecasting outcomes.
  - `portfolio_optimization.py`: Computes risk/return metrics and optimizes portfolio allocation.
  - `utils.py`: Utility functions for data handling and visualization.

- **models/**: Stores trained forecasting models for easy reusability.
  - `trained_model_arima.pkl`: Saved ARIMA model.
  - `trained_model_sarima.pkl`: Saved SARIMA model.
  - `trained_model_lstm.h5`: Saved LSTM model.
  - `model_selection_notes.md`: Details on model selection criteria and parameter tuning.

- **results/**: Contains visualizations, analysis reports, and summaries of findings.
  - `eda_visualizations/`: Stores plots from EDA.
  - `forecast_visualizations/`: Contains plots of forecasted trends.
  - `portfolio_performance/`: Visualizes portfolio metrics such as risk-return analysis.
  - `analysis_report.md`: Consolidates key findings and conclusions.

- **requirements.txt**: Lists all dependencies required for the project to ensure consistent environment setup.

- **references/**: Research notes, methodologies, and literature references used in this project.
  - `time_series_forecasting.md`: Notes on time series forecasting methodologies.
  - `portfolio_optimization.md`: Overview of portfolio optimization techniques.
  - `literature/`: Directory for academic papers and resources.

### Usage Instructions

1. **Set Up Environment**: Install required packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
