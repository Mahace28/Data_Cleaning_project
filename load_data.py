import pandas as pd

def load_dataset():
    df = pd.read_csv("StudentsPerformance.csv")
    return df