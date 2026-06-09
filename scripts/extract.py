import pandas as pd

df = pd.read_csv(
    "data/orders.csv",
    encoding="latin1"
)

print("\nColumns:\n")
print(df.columns)

print("\nShape:\n")
print(df.shape)

print("\nMissing Values:\n")
print(df.isnull().sum())