import pandas as pd

def transform_data():

    df = pd.read_csv(
        "data/orders.csv",
        encoding="latin1"
    )

    print("Original Shape:", df.shape)
    

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Delivery time
    df["Delivery Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # Revenue after discount
    df["Net Sales"] = (
        df["Sales"] * (1 - df["Discount"])
    )

    # Time dimensions
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Quarter"] = df["Order Date"].dt.quarter

    print("\nTransformed Shape:", df.shape)

    return df

if __name__ == "__main__":
    df = transform_data()

    print(df.head())
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)    
    
df.to_csv(
    "data/cleaned_orders.csv",
    index=False
)

print("Cleaned dataset saved")    