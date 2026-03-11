# vis/visualizations.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_visualizations():

    print("Creating visualizations...")

    # Load model results
    df = pd.read_csv("data/model_outputs/model1_predictions.csv")

    # Confusion-style comparison chart
    sns.countplot(x="Actual", hue="Predicted", data=df)

    plt.title("Model Prediction vs Actual Diabetes Mortality Classification")
    plt.xlabel("Actual Classification")
    plt.ylabel("Count")

    # Save visualization
    plt.savefig("data/visualizations/model1_results.png")

    plt.show()

    print("Visualization saved to data/visualizations")
