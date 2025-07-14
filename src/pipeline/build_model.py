# src/pipeline/build_model.py

import joblib
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def read_df(filepath):
    """
    Read the dataframe from the filepath
    """
    return pd.read_csv(filepath)

def preprocess_data(df):
    """
    Preprocess the data
    """
    # Features / Target
    X = df[["company", "gender", "position_level", "performance_score", "work_hours_per_week", "experience_years", "has_certifications", "promoted"]]
    y = df["salary"]
   
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train_evaluate_model(X_train, X_test, y_train, y_test, model):
    """
    Train and evaluate the model
    """
    # Training
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    mae = np.mean(np.abs(y_test - y_pred))
    mse = np.mean((y_test - y_pred)**2)
    rmse = np.sqrt(np.mean((y_test - y_pred)**2))
    r2 = r2_score(y_test, y_pred)
    print(f"MAE Score: {mae}\nMSE Score: {mse}\nRMSE Score: {rmse}\nR^2 Score: {r2}")

    return model

if __name__ == "__main__":
    df = read_df('./data/prepared_people.csv')
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    model = LinearRegression()
    model = train_evaluate_model(X_train, X_test, y_train, y_test, model)



    # Save
    dir_path = './models'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Scaler
    joblib.dump(scaler, f'{dir_path}/scaler.pkl')
    # Model
    joblib.dump(model, f'{dir_path}/model.pkl')
