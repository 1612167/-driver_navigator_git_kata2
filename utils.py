import pandas as pd
import numpy as np

def load_passengers():
    # Load the Titanic dataset
    df = pd.read_csv('data/titanic.csv')

    # Select only the male passengers
    male_passengers = df[df['Sex'] == 'male']

    return male_passengers