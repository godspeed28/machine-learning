import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# baca dataset
file_path = 'data/iris_data.csv'
data = pd.read_csv(file_path)

# === 1️⃣ Scatter Plot: Sepal vs Petal ===
plt.figure(figsize=(6, 5))
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='Sepal', alpha=0.7)
plt.plot(data.petal_length, data.petal_width, ls='', marker='x', label='Petal', alpha=0.7)

plt.xlabel('Length (cm)')
plt.ylabel('Width (cm)')
plt.title('Iris Flower Dimensions (Sepal vs Petal)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# === 2️⃣ Histogram: Distribusi Sepal Length ===
plt.figure(figsize=(6, 4))
plt.hist(data.sepal_length, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# === 3️⃣ Horizontal Bar Chart: 10 Sample Sepal Widths ===
fig, ax = plt.subplots(figsize=(6, 4))
samples_to_plot = min(10, len(data))  # hindari error kalau data < 10
ax.barh(np.arange(samples_to_plot), data.sepal_width.iloc[:samples_to_plot], color='lightgreen', edgecolor='black')

# set ticks dan label
yticks = np.arange(samples_to_plot)
ax.set_yticks(yticks)
ax.set_yticklabels(np.arange(1, samples_to_plot + 1))

# label dan judul
ax.set(xlabel='Width (cm)', ylabel='Sample Index', title='Iris Sepal Widths (First 10 Samples)')
plt.tight_layout()
plt.show()
