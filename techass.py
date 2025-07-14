import pandas as pd
import matplotlib.pyplot as plt

# The dataset 
data = {
    'Month': [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],
    'Laptops': [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 190, 200],
    'Smartphones': [200, 220, 250, 270, 260, 300, 310, 295, 280, 270, 320, 350],
    'Tablets': [90, 95, 100, 110, 105, 115, 120, 118, 112, 109, 125, 130],
    'Monitors': [60, 62, 65, 68, 66, 70, 75, 73, 72, 70, 78, 80],
    'Keyboards': [40, 42, 45, 47, 46, 48, 50, 49, 47, 46, 51, 55],
    'Mouse': [38, 39, 41, 42, 41, 43, 44, 43, 42, 41, 45, 47]
}

df = pd.DataFrame(data)

#Get total yearly sales for each product
yearly_sales = df.drop('Month', axis=1).sum()

#Plot bar chart
yearly_sales.plot(kind='bar', color='lightblue')

#Add labels and show
plt.title("Total Yearly Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Units Sold")
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Line chart for smartphone sales
df.plot(x='Month', y='Smartphones', kind='line', marker='o', color='orange')

# Add labels and title
plt.title("Monthly Smartphone Sales Trend")
plt.xlabel("Month")
plt.ylabel("Smartphones Sold")
plt.grid(True)
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Create a histogram of tablet sales
df['Tablets'].plot(kind='hist', bins=5, color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Distribution of Tablet Sales")
plt.xlabel("Tablet Sales Range")
plt.ylabel("Number of Months")
plt.grid(True)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Scatter plot: Mouse vs Keyboard sales
df.plot(x='Mouse', y='Keyboards', kind='scatter', color='green')

# Add labels and title
plt.title("Mouse vs Keyboard Sales")
plt.xlabel("Mouse Sales")
plt.ylabel("Keyboard Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


df.to_csv('tech_store_sales.csv', index=False)



