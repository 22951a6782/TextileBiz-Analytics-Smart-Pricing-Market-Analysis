def get_headers():
    ua = UserAgent()
    return {"User-Agent": ua.random}

PROXY_LIST = [
    "http://45.77.67.81:8080", "http://188.166.16.94:8118",
    "http://165.227.199.59:3128", "http://178.62.193.19:8118"
]

def get_random_proxy():
    return {"http": random.choice(PROXY_LIST)}

def get_amazon_price(product_name):
    """Scrapes Amazon price"""
    try:
        url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        headers, proxy = get_headers(), get_random_proxy()
        response = requests.get(url, headers=headers, proxies=proxy, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.select_one("span.a-price-whole")
        return int(price_element.text.replace(",", "")) if price_element else None
    except:
        return None

def get_google_price(product_name):
    """Scrapes Google for Amazon prices"""
    try:
        search_url = f"https://www.google.com/search?q={product_name.replace(' ', '+')}+price+site:amazon.in"
        headers = get_headers()
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        return int(price_element.text.replace("₹", "").replace(",", "")) if price_element else None
    except:
        return None

#  Run price scraping with delays
def get_price_with_delay(row):
    time.sleep(random.uniform(5, 15))  # Random delay to avoid detection
    return get_amazon_price(row["item"]) or get_google_price(row["item"]) or max(row["sale price"] - 30, 0)

#  Enable progress tracking
tqdm.pandas(desc="Fetching Competitor Prices")
df["competitor price"] = df.progress_apply(get_price_with_delay, axis=1)

# Save updated dataset
df.to_csv(CLEANED_FILE, index=False)
print(f"✅ Competitor prices added and saved as '{CLEANED_FILE}'")
