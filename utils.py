import pandas as pd
import numpy as np

def load_passengers():
    # Load the Titanic dataset
    df = pd.read_csv('data/titanic.csv')

<<<<<<< HEAD
    # Select only the female passengers
    female_passengers = df[df['Sex'] == 'male']
=======
    # Select only the male passengers
    male_passengers = df[df['Sex'] == 'male']
>>>>>>> 365fa7cc67462b977869c778d0926867f0d81b35

    return male_passengers