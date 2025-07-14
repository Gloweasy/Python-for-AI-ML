import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv('student_scores.csv')

# 2. Define features and label
X = df[['Hours_Studied']]
y = df['Exam_Score']

# 3. Split data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict exam scores for test data
y_pred = model.predict(X_test)

# 6. Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("📊 Model Evaluation")
print("-------------------")
print("Mean Squared Error (MSE):", round(mse, 2))
print("R² Score:", round(r2, 2))

# 7. Predict for 7.25 hours
new_hours = [[7.25]]
predicted_score = model.predict(new_hours)
print("\n📈 Predicted score for a student who studied 7.25 hours:", round(predicted_score[0], 2))

# 8. Visualize the data and regression line
plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Hours vs Exam Score')
plt.legend()
plt.grid(True)
plt.show()
