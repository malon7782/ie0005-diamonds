import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.neighbors import LocalOutlierFactor
import joblib

df = pd.read_csv('diamonds.csv')
df = df.dropna()
df = df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)]

# replace non-numeric values with numeric ones

cut_mapping = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_mapping = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
clarity_mapping = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

df['cut_encoded'] = df['cut'].map(cut_mapping)
df['color_encoded'] = df['color'].map(color_mapping)
df['clarity_encoded'] = df['clarity'].map(clarity_mapping)

# train the LinearRegression model

features = ['carat', 'cut_encoded', 'color_encoded', 'clarity_encoded', 'depth', 'x', 'y', 'z']
X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# evaluation

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R^2: {r2:.4f}")
print(f"MAE: ${mae:.2f}")

# !find best deals

results = X_test.copy()
results['actual_price'] = y_test
results['predicted_price'] = y_pred.round(2)
results['difference'] = results['actual_price'] - results['predicted_price']

lof = LocalOutlierFactor(novelty = True, n_neighbors = 20)
lof.fit(X_train)
results['is_normal'] = lof.predict(X_test)

good_deals = results[(results['difference'] < 0) & (results['is_normal']) == 1]

# pack and save the models

model_filename = 'diamond_models.pkl'

models = {
    'price_model': model,
    'outlier_model': lof
}

joblib.dump(models, model_filename)

