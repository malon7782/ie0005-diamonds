import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
sb.set()

df = pd.read_csv('diamonds.csv')

# basic data cleaning; drop rows with garbage values &&

initial_shape = df.shape
df = df.dropna()
df = df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)]
cleaned_shape = df.shape
print(f"inital: {initial_shape}")
print(f"cleaned: {cleaned_shape}")
print(f"droped {initial_shape[0] - cleaned_shape[0]}")

# discribe()

print("\nDescribe():")
print(df.describe().round(2))

# diagrams: numeric values

# price distribution

plt.figure(figsize = (18, 5))

plt.subplot(1, 3, 1)
sb.histplot(df['price'], kde = True)
plt.title('price distribution')
plt.ylabel('price')
plt.ylabel('count')

# carat distribution

plt.subplot(1, 3, 2)
sb.histplot(df['carat'], kde=True)
plt.title('carat weight distribution')
plt.xlabel('carat')
plt.ylabel('count')

# heatmap

plt.subplot(1, 3, 3)
numeric = df.select_dtypes(include=['float64', 'int64'])
corr = numeric.corr()

sb.heatmap(corr, annot = True, fmt = '.2f', square = True)
plt.title('correlation heatmap')

plt.show()

# diagram: non-numeric values

plt.figure(figsize=(18, 5))

cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
plt.subplot(1, 3, 1)
sb.boxplot(x='cut', y='price', data=df, order=cut_order, palette='Set2')
plt.title('price vs cut')

color_order = ['J', 'I', 'H', 'G', 'F', 'E', 'D'] 
plt.subplot(1, 3, 2)
sb.boxplot(x='color', y='price', data=df, order=color_order, palette='Set2')
plt.title('price vs color')

clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
plt.subplot(1, 3, 3)
sb.boxplot(x='clarity', y='price', data=df, order=clarity_order, palette='Set2')
plt.title('price vs clarity')

plt.show()
