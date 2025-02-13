#  Load optimized dataset
df = pd.read_csv(OPTIMIZED_PRICING_FILE)

# Generate "total_sales" based on season & item type
def generate_seasonal_sales(row):
    base_sales = np.random.randint(50, 150)
    if "cotton" in row["item"].lower() and "summer" in row["season"].lower():
        return np.random.randint(200, 500)
    elif "sweater" in row["item"].lower() and "winter" in row["season"].lower():
        return np.random.randint(250, 600)
    else:
        return base_sales

df["total_sales"] = df.apply(generate_seasonal_sales, axis=1)

#  Select Features & Target Variable
features = ["cost price", "sale price", "competitor price", "total_sales"]
target = "optimized price"

#  Drop rows with missing values
df = df.dropna(subset=features + [target])

#  Train-Test Split
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Train Model
model = LinearRegression()
model.fit(X_train, y_train)

#  Save Model
with open(MODEL_FILE, "wb") as file:
    pickle.dump(model, file)

print(f"✅ Model saved successfully as {MODEL_FILE}!")

# Save final dataset
df.to_csv(FINAL_ML_PREDICTION_FILE, index=False)
print(f"✅ ML-Predicted pricing dataset saved as {FINAL_ML_PREDICTION_FILE}")
