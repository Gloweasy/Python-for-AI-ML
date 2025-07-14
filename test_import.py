#import greetings_module

#print("Now running test_module.py")

import pandas as pd

# Try to read the CSV file
df = pd.read_csv('student_scores.csv')

# Show the first few rows
print("📄 Your CSV file looks like this:\n")
print(df.head())
