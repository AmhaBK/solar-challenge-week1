import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

benin= pd.read_csv(r"C:\Users\mike\Documents\Kifiya_AIM\data\benin-malanville.csv", parse_dates=["Timestamp"])
sierraleone= pd.read_csv(r"C:\Users\mike\Documents\Kifiya_AIM\data\sierraleone-bumbuna.csv", parse_dates=["Timestamp"])
togo= pd.read_csv(r"C:\Users\mike\Documents\Kifiya_AIM\data\togo-dapaong_qc.csv", parse_dates=["Timestamp"])

print(benin.head())
print(benin.describe())
print(sierraleone.head())
print(sierraleone.describe())
print(togo.head())
print(togo.describe())

print(benin.isna().sum())
print(sierraleone.isna().sum())
print(togo.isna().sum())

print(benin.dtypes)
print(sierraleone.dtypes)
print(togo.dtypes)

