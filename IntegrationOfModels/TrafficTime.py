import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import seaborn as sns
import numpy as np

# Load the data
pd.pandas.set_option('display.max_columns',None)
df = pd.read_csv(r"D:/Btech_AI/4thsem/AI/Project/IntegrationOfModels/data.csv")
# one-hot encoding categorical variables
df = pd.get_dummies(df, columns=['sourceid', 'destid']) 

# Split the data into features (X) and targets (y)
X = df.drop(['duration', 'duration_in_traffic'], axis=1)
y = df[['duration', 'duration_in_traffic']]
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
# Create and fit the model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
# Make predictions on the test set
y_pred_rf = rf_model.predict(X_test)

from joblib import dump

# Save the model to a file
dump(rf_model, 'random_forest_model.joblib')




