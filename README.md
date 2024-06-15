# Predicting and Forecasting Temperature using Multiple-Linear Regression in CAMANAVA

## Dataset
- **Title:** Philippine Major Cities Weather Data ☀️
- **Source:** [Kaggle](https://doi.org/10.34740/KAGGLE/DS/3990689)

## Preprocessing
1. **Checking for Null Values:**
   - Ensure there are no missing values in the dataset.
   
2. **Getting Data from CAMANAVA:**
   - Extract data specifically for the cities of Caloocan, Malabon, Navotas, and Valenzuela.

3. **Setting Datetime as Index:**
   - Convert the `datetime` column to the index of the DataFrame.

4. **Encoding Categorical Data:**
   - Use one-hot encoding for the `weather.id` column to handle categorical data.

## Model Training
### Separating the Features
- **Dependent Variable:**
  - Temperature: `main.temp`

- **Independent Variables:**
  - Datetime: `datetime` (format: YYYY-MM-DD HH:MM:SS UTC+08:00)
  - Atmospheric Pressure: `main.pressure` (hPa, on the sea level)
  - Humidity: `main.humidity` (%)
  - Cloudiness: `clouds.all` (%)
  - Weather Condition: `weather.id`
  - Wind Speed: `wind.speed`

### Data Splitting
- Split the dataset into training and testing sets, preserving temporal data, with an 80/20 ratio.

### Model Initialization and Training
- Initialize and train the Linear Regression model using the training dataset.

## Model Testing and Evaluation
1. **Testing on the Test Set:**
   - Evaluate the model performance using the test dataset.

2. **Evaluation Metrics:**
   - **Mean Squared Error (MSE):**
     - Measures the average squared difference between the predicted values and the actual (observed) values.
   - **Mean Absolute Error (MAE):**
     - Measures the average absolute difference between predicted and actual values, providing a straightforward measure of prediction accuracy.
   - **Root Mean Squared Error (RMSE):**
     - Measures the square root of the average squared difference between predicted and actual values, providing a comparable metric in the original scale of the data.

