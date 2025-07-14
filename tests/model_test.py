# tests/model_test.py

import numpy as np
import joblib
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split

@pytest.fixture
def model():
    return joblib.load('./models/model.pkl')

@pytest.fixture
def scaler():
    return joblib.load('./models/scaler.pkl')

@pytest.fixture
def test_data_and_target():
    # Load the same dataset used for training
    df = pd.read_csv('./data/prepared_people.csv')
    
    # Use the same features and target as in model training
    X = df[["company", "gender", "position_level", "performance_score", 
            "work_hours_per_week", "experience_years", "has_certifications", "promoted"]]
    y = df["salary"]
    
    # Use the same train/test split as in model training (same random_state)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_test, y_test

def test_model_mae(model, scaler, test_data_and_target):
    X_test, y_test = test_data_and_target
    
    # Apply the same scaling as during training
    X_test_scaled = scaler.transform(X_test)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate MAE
    mae = np.mean(np.abs(y_test - y_pred))
    
    # Assert that MAE is reasonable (same threshold as before)
    assert mae < 9000