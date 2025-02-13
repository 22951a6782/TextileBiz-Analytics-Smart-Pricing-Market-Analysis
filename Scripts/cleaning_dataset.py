
import os
import time
import random
import pandas as pd
import requests
import numpy as np
import pickle
from tqdm import tqdm
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -------------------- CONFIG --------------------
RAW_FILE = "Textile_data2.txt.csv"
CLEANED_FILE = "Enhanced_Textile_Dataset.csv"
PRICING_ANALYSIS_FILE = "Pricing_Analysis_Report.csv"
OPTIMIZED_PRICING_FILE = "Optimized_Pricing_Dataset.csv"
FINAL_ML_PREDICTION_FILE = "Final_ML_Pricing_Dataset.csv"
MODEL_FILE = "trained_model.pkl"

# Load dataset
if not os.path.exists(RAW_FILE):
    raise FileNotFoundError(f"❌ File '{RAW_FILE}' not found!")

df = pd.read_csv(RAW_FILE)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Check for missing columns
required_columns = ["item", "cost price", "sale price", "mrp", "quality", "availability", "season", "location"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise KeyError(f"❌ Missing columns: {missing_columns}")

# Remove missing values
df = df.dropna(subset=["item", "sale price"])

# Save cleaned dataset
df.to_csv(CLEANED_FILE, index=False)
print(f"✅ Cleaned dataset saved as '{CLEANED_FILE}'")
