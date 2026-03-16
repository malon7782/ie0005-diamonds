import pandas as pd
import joblib


models = joblib.load('diamond_models.pkl')
price_model = models['price_model']
outlier_model = models['outlier_model']

# cut(1:Fair ➔ 5:Ideal) | Color(1:J ➔ 7:D) | clarity(1:I1, 2:SI2, 3:SI1, 4:VS2, 5:VS1, 6:VVS2, 7:VVS1, 8:IF)

user_input = {
    'carat': 0.9, 
    'cut_encoded': 5,      # Ideal
    'color_encoded': 4,    # G
    'clarity_encoded': 4,  # VS2
    'depth': 62.0, 
    'x': 6.1, 
    'y': 6.15, 
    'z': 3.8
}
    
seller_price = 3500  

df_input = pd.DataFrame([user_input])
    
features = ['carat', 'cut_encoded', 'color_encoded', 'clarity_encoded', 'depth', 'x', 'y', 'z']
df_input = df_input[features]

predicted_price = price_model.predict(df_input)[0]
is_normal = outlier_model.predict(df_input)[0]

print(f"sold for: ${seller_price:.2f}")
print(f"predicted actual price: ${predicted_price:.2f}")

if is_normal == -1:
    print("\nWARNING: It's most likely a defective product. Please buy with caution.")

diff = seller_price - predicted_price
if diff < -0.1 * seller_price:
    print(f"Good deal. (${abs(diff):.2f} lower)")
elif 0.1 * seller_price < diff:
    print(f"Not a good deal. (${diff:.2f} higher)")

