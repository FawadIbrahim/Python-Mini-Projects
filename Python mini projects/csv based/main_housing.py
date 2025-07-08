import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("csv based/Housing_price.csv")

# Strip and rename column names for consistency
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Preview column names
print("Columns:", df.columns)

# Define price cleaner
def clean_price(price_str):
    try:
        price_str = str(price_str).lower().replace("pkr", "").strip()

        if "crore" in price_str:
            num = float(price_str.replace("crore", "").strip())
            return num * 10000000
        elif "million" in price_str:
            num = float(price_str.replace("million", "").strip())
            return num * 1000000
        elif "lakh" in price_str:
            num = float(price_str.replace("lakh", "").strip())
            return num * 100000
        else:
            return float(price_str.replace(",", ""))
    except:
        return None

# Apply cleaner
df["clean_price"] = df["price"].apply(clean_price)

# Drop missing prices
df = df.dropna(subset=["clean_price", "city"])

# Group by city
avg_price = df.groupby("city")["clean_price"].mean().sort_values(ascending=False)

# Print result
print("\n Average Price by City (in PKR):\n")
print(avg_price)

# Plot
plt.figure(figsize=(12, 6))
avg_price.plot(kind="bar", color="skyblue")
plt.title("Average Housing Price by City")
plt.ylabel("Average Price (PKR)")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


