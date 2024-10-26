# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print("Dataset:")
print(df.head())

# Calculate and display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Plot a graph of a specific column
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o')
plt.title('Value over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
