
# Model Selection and Parameter Tuning Notes

## ARIMA Model
- **Order (p, d, q)**: (1, 1, 1)
- **Model Selection Rationale**: Chosen for univariate forecasting with no seasonality.
- **Evaluation Metrics**:
  - MAE: 0.10
  - RMSE: 0.11
  - MAPE: 3.60%
- **Observations**: ARIMA effectively captures short-term trends but may have limited performance in capturing volatility and complex seasonal patterns.

---

## SARIMA Model
- **Order (p, d, q)**: (1, 1, 1)
- **Seasonal Order (P, D, Q, m)**: (1, 1, 1, 12)
- **Model Selection Rationale**: Selected to account for monthly seasonality.
- **Evaluation Metrics**:
  - MAE: 0.10
  - RMSE: 0.10
  - MAPE: 3.37%
- **Observations**: SARIMA performed slightly better than ARIMA, especially in accounting for seasonality. It showed slightly lower error rates, indicating improved performance in capturing cyclical patterns.

---

## LSTM Model
- **Architecture**: 2 LSTM layers with 50 units each, followed by dense layers.
- **Sequence Length**: 60 days (sliding window for input).
- **Training Epochs**: 50
- **Batch Size**: 32
- **Evaluation Metrics**:
  - MAE: 0.065
  - RMSE: 0.080
  - MAPE: 4.15%
- **Observations**: LSTM achieved the lowest MAE and RMSE, showcasing superior performance for capturing long-term dependencies. However, its MAPE is slightly higher than SARIMA, suggesting some sensitivity to large errors relative to true values. 

---

## Summary
- **Best Model**: While LSTM had the lowest MAE and RMSE, SARIMA achieved the lowest MAPE, indicating better error distribution relative to true values. The choice of model could depend on the specific forecasting needs:
  - **Use LSTM**: When capturing complex patterns and long-term dependencies is essential.
  - **Use SARIMA**: For reliable performance with lower relative error in simpler cyclical patterns.
  
This summary provides a nuanced view of model strengths and guides their application based on forecasting objectives.
