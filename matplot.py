import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Name': ['Alice', 'Bob', 'Clara', 'David', 'Eva'],
    'Age': [15, 16, 15, 17, 16],
    'Gender': ['F', 'M', 'F', 'M', 'F'],
    'Math_Score': [88, 75, 90, 65, 85],
    'Reading_Score': [92, 85, 95, 70, 89]
}

df = pd.DataFrame(data)

# Explore the dataset
print(df.head())
print(df.describe())


plt.hist(df['Math_Score'], bins=5, color='skyblue', edgecolor='black')
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()
