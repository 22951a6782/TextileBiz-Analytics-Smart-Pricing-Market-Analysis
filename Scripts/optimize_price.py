# Define Pricing Rules
def adjust_price(row):
    sale_price = row["sale price"]
    competitor_price = row["competitor price"]
    cost_price = row["cost price"]

    if pd.isna(competitor_price) or competitor_price <= 0:
        return sale_price  # No competitor price, keep original

    price_gap = sale_price - competitor_price
    min_profit_margin = cost_price * 1.2  # Ensure 20% profit

    if price_gap > 30:
        return max(competitor_price + 10, min_profit_margin)  # Reduce price
    elif price_gap < -30:
        return min(competitor_price - 10, sale_price * 1.1)  # Increase price
    else:
        return sale_price  # Keep same

df["optimized price"] = df.apply(adjust_price, axis=1)

#  Save Optimized Pricing Dataset
df.to_csv(OPTIMIZED_PRICING_FILE, index=False)
print(f"✅ Optimized pricing dataset saved as {OPTIMIZED_PRICING_FILE}")
