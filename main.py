# weather_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('seattle-weather.csv')

# Drop the 'date' column (not needed for current analysis)
df = df.drop('date', axis=1)

# Count different weather types and plot
weather_counts = df['weather'].value_counts()

plt.figure(figsize=(8, 5))
weather_counts.plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.title('Weather Condition Distribution in Seattle')
plt.xlabel('Weather Type')
plt.ylabel('Frequency')
plt.tight_layout()

# Save the plot (optional)
plt.savefig('charts/weather_distribution.png')

plt.show()
