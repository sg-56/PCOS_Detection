#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
from imblearn.over_sampling import SMOTE

import os


# Load data
DATA_DIR = '../data/cleaned_data.csv'
df = pd.read_csv(DATA_DIR)

# Clean column names
df.columns = [col.replace(' ', '_') for col in df.columns]

# Handle missing values
df['Acne_Severity'].fillna('NA', inplace=True)

# Drop unnecessary columns
df = df.drop(columns=['Undiagnosed_PCOS_Likelihood'])

# Separate features and target
X = df.drop(columns=['Diagnosis'])
y = df['Diagnosis']

# Identify column types
cat_cols = X.select_dtypes(include='object').columns
num_cols = X.select_dtypes(include='number').columns.to_list()
ordinal_cols = ['BMI', 'Acne_Severity', 'Stress_Levels', 'Socioeconomic_Status']
nominal_cols = [col for col in cat_cols if col not in ordinal_cols]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Preprocessing pipeline
transformer = ColumnTransformer([
    ('Numerical_pipeline', StandardScaler(), num_cols),
    ('Nominal_cols', OneHotEncoder(), nominal_cols),
    ('Ordinal_cols', OrdinalEncoder(), ordinal_cols),
], remainder='passthrough')

# Fit and transform the training data
transformer.fit(X_train)

X_train_tr = transformer.transform(X_train)
X_test_tr = transformer.transform(X_test)

smote = SMOTE()
X_train_sm,y_train_sm = smote.fit_resample(X_train_tr,y_train)
print(f"Shape of X_train after Super Sampling : {X_train_sm.shape,y_train_sm.shape}")

# Train the model
model = RandomForestClassifier(
    n_estimators=400,
    max_depth=10,
    n_jobs=-1,
    random_state=42
)
model.fit(X_train_sm, y_train_sm)

# Evaluate the model
y_pred = model.predict(X_test_tr)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# Save artifacts
os.makedirs('../backend/artifacts', exist_ok=True)

with open('../backend/artifacts/preprocessor.pkl', 'wb') as file:
    pickle.dump(transformer, file)

with open('../backend/artifacts/model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model and preprocessor saved successfully.")
