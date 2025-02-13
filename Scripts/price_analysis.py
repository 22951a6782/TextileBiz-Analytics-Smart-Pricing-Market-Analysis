# Compute Price Differences
df["price_difference"] = df["sale price"] - df["competitor price"]

# Classify Items Based on Pricing
def classify_price_status(row):
    if row["price_difference"] > 30:
        return "Overpriced"
    elif row["price_difference"] < -30:
        return "Underpriced"
    else:
        return "Competitive"

df["price_status"] = df.apply(classify_price_status, axis=1)

#  Save Analysis Report
df.to_csv(PRICING_ANALYSIS_FILE, index=False)
print(f"✅ Pricing Analysis Report saved as {PRICING_ANALYSIS_FILE}")
