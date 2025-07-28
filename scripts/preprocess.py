# Simple mobile-friendly preprocessing
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/gb1.csv')

# Simple cleaning
df = df[['sequence', 'fitness']].dropna()
df['sequence'] = df['sequence'].str.upper()

# Save cleaned data
df.to_csv('../data/processed/gb1_processed.csv', index=False)
print("Success! File saved.")