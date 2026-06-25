import numpy as np
import pandas as pd

df = pd.read_csv("products_dataset.csv")
print(df)

average_price = np.mean(df["Price"])
print("\nAverage Price =", average_price)


def above_average():
    print("\nProducts Priced Above Average:")
    for i in range(len(df)):
        if df["Price"][i] > average_price:
            print(df["Product Name"][i], "-", df["Price"][i])

above_average()

#Question2
df = pd.read_csv("daily_temperature_dataset.csv")
print(df)

highest = np.max(df["Temperature (°C)"])
lowest = np.min(df["Temperature (°C)"])
average = np.mean(df["Temperature (°C)"])

print("\nHighest Temperature =", highest, "°C")
print("Lowest Temperature =", lowest, "°C")
print("Average Temperature =", average, "°C")

def classify(temp):
    if temp < 20:
        return "Cold"
    elif temp <= 30:
        return "Moderate"
    else:
        return "Hot"

print("\nTemperature Category:")
for i in range(len(df)):
    day = df["Day"][i]
    temp = df["Temperature (°C)"][i]
    print(day, "-", temp, "°C :", classify(temp))