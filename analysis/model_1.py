# analysis/model_1.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


def run_model_1():

    print("Running Model 1...")

    # Load transformed data
    df = pd.read_csv("data/transformed/clean_diabetes_data.csv")

    # Example target variable
    # Create a binary classification: high vs low death rate
    median_rate = df["age_adjusted_death_rate"].median()
    df["high_death_rate"] = df["age_adjusted_death_rate"] > median_rate

    # Features and target
    X = df[["average_annual_count"]]  
    y = df["high_death_rate"]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    print("Accuracy:", accuracy)
    print(report)

    # Save model results
    results = pd.DataFrame({
        "Actual": y_test,
        "Predicted": predictions
    })

    results.to_csv("data/model_outputs/model1_predictions.csv", index=False)

    print("Model outputs saved to data/model_outputs")

    return accuracy
