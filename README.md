# 🏷️ TextileBiz Analytics: Smart Pricing & Market Analysis  

*TextileBiz Analytics* is an advanced *data-driven pricing optimization* solution designed for the textile industry. This project leverages *real-time price scraping, competitive market analysis, dynamic pricing strategies, and machine learning* to help businesses make informed pricing decisions.  

## 🚀 Features  

### 🔹 *Data Preprocessing & Cleaning*  
- Standardizes and prepares raw textile pricing data for analysis.  
- Removes missing values and normalizes column formats.  

### 🔹 *Competitor Price Scraping*  
- Extracts real-time pricing data from *Amazon & Google*.  
- Uses automated web scraping techniques with proxy support.  

### 🔹 *Pricing Analysis & Classification*  
- Identifies *overpriced, underpriced, and competitive* items.  
- Generates detailed pricing analysis reports.  

### 🔹 *Dynamic Pricing Optimization*  
- Applies *business rules* to adjust pricing based on competitors.  
- Ensures minimum profit margins and strategic price reductions.  

### 🔹 *Machine Learning Model for Price Prediction*  
- Trains a *Linear Regression Model* to predict optimized prices.  
- Factors in *cost price, competitor price, seasonality, and location*.  

### 🔹 *Published Power BI Dashboard for Insights*  
- Provides interactive *visual analytics* for pricing trends.  
- Showcases *competitor benchmarking* and *optimal price recommendations*.  
- Access the published dashboard [here](https://app.powerbi.com/groups/me/reports/2463b25e-78d9-4a68-b252-e803860fe98c?ctid=b45e253c-d9f0-4c81-b778-8d3197741240&pbi_source=linkShare).  

---

## 📂 Folder Structure  

bash
TextileBiz-Analytics-Smart-Pricing-Market-Analysis/
│── data/
│   ├── Textile_data2.txt.csv  # Original raw dataset
│   ├── Enhanced_Textile_Dataset.csv  # Cleaned dataset
│   ├── Pricing_Analysis_Report.csv  # Pricing classification results
│   ├── Optimized_Pricing_Dataset.csv  # Adjusted pricing after rules
│   ├── Final_ML_Pricing_Dataset.csv  # ML-predicted optimal prices
│── models/
│   ├── trained_model.pkl  # Trained Machine Learning model
│── scripts/
│   ├── cleaning_dataset.py  # Data cleaning & preprocessing
│   ├── price_scraper.py  # Web scraping (Amazon & Google)
│   ├── price_analysis.py  # Competitive pricing classification
│   ├── optimize_price.py  # Dynamic pricing strategy implementation
│   ├── train_model.py  # Machine Learning model training
│── notebooks/
│   ├── TextileBiz_Analytics_Analysis.ipynb  # Jupyter Notebook with full pipeline
│── dashboards/
│   ├── screenshots/
│       ├── dashboard1.png  # dashboard view
│       ├── dashboard2.png  # dashboard view
│       ├── dashboard3.png  # dashboard view
│   ├── Textile_Pricing_Dashboard.pbix  # Power BI Dashboard file
│── templates/
│   ├── dashboard.html  # Frontend to access the published Power BI dashboard
│── app.py  # Flask application to serve dashboard
│── README.md  # Project documentation
│── requirements.txt  # Python dependencies

---

## 📊 Power BI Dashboard  
📌 The *Textile_Pricing_Dashboard.pbix* file in the dashboards/ folder provides:  
✔ *Market Trends* | ✔ *Price Competitiveness* | ✔ *Optimized Pricing Insights*  

To use:  
- Open *Power BI Desktop*.  
- Load dashboards/Textile_Pricing_Dashboard.pbix.  
- Analyze *pricing trends, competitor insights, and ML-based pricing predictions*.  

Alternatively, access the published version directly from the web [here](https://app.powerbi.com/groups/me/reports/2463b25e-78d9-4a68-b252-e803860fe98c?ctid=b45e253c-d9f0-4c81-b778-8d3197741240&pbi_source=linkShare).  
Note: you have to login through your organisation domain to access through web

---

## ⚙️ Configuration  
The config/config.yaml file stores key parameters, including:  
🔹 Pricing adjustment rules  
🔹 Web scraping settings  
🔹 Machine learning hyperparameters  

Modify this file to *customize your pricing strategy*.

---

## 🛠️ Technologies Used  
- *Backend:* Flask  
- *Data Processing:* Pandas, NumPy  
- *Web Scraping:* BeautifulSoup, Requests, Fake-UserAgent  
- *Machine Learning:* Scikit-Learn (Linear Regression)  
- *Visualization:* Power BI  
- *Development Tools:* Python, Jupyter Notebook  

---

## 📝 Testing & Validation  
- *Data Quality Checks* – Ensures clean and structured data.  
- *Model Evaluation* – Validates accuracy of pricing predictions.  
- *Competitor Benchmarking* – Verifies scraped data against actual market prices.  

---

## 📝 Running the Flask Application  

### 🔧 Installation & Setup  

1️⃣ Install dependencies:  
bash
pip install -r requirements.txt


2️⃣ Run the Flask app:  
bash
python app.py


3️⃣ Open the browser and go to:  

http://127.0.0.1:5000/

This will render the *dashboard.html* template with a button linking to the *published Power BI dashboard*.  

---

## 📬 Contact & Support  
*Developed by:* Pranitha Perala  
- *Email:* peralapranitha17@gmail.com  
- *LinkedIn:* [My Profile](https://github.com/22951a6782/TextileBiz-Analytics-Smart-Pricing-Market-Analysis)  

---

## 🚀 Transform Your Textile Business with Smart Pricing Strategies!
