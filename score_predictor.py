import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Scores': [35, 40, 45, 50, 55, 60, 65, 70, 75]
}
df = pd.DataFrame(data)

X = df[['Hours_Studied']]  # input features (must be 2D)
y = df['Scores']           # target label

model = LinearRegression()
model.fit(X, y)

hours = [[5]]  # let's predict for a student who studied 5 hours
predicted_score = model.predict(hours)

print(f"If a student studies for 5 hours, the predicted score is: {predicted_score[0]:.2f}")

# Step 5: Optional - Show the plot
plt.scatter(X, y, color='blue', label='Actual scores')
plt.plot(X, model.predict(X), color='red', label='Predicted line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours vs Score')
plt.legend()
plt.show()