import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# direct path to directory with csv and stan files
direct_path = os.path.dirname(__file__)

# Import Data1.csv file to python.
# Set first column as the index.
df = pd.read_csv(os.path.join(direct_path, 'Data1.csv'), sep=',', index_col=0, parse_dates=True)
print(df.head())
print(df.info())

# Plot all columns as time series.
df.plot(subplots=True)
plt.suptitle("All columns as time series")
plt.show(block=False)

# Plot histograms of all columns
df.hist()
plt.suptitle("Histograms of all columns")
plt.show(block=False)

# Plot all on a single, faceted plot.
df.plot()
plt.suptitle("All columns on a single, faceted plot")
plt.show(block=False)

# Plot KDE-s (Kernel Denisty Estimators) for all columns.
df.plot.density(subplots=True)
plt.suptitle("KDE-s for all columns")
plt.show(block=False)

# Repeat analysis for columns $\theta_1$-$\theta_4$ in 2018.
print("now analyse for 2018")
df_new = df.loc['2018']
df_th1_4_18 = df.loc['2018', 'theta_1':'theta_4']
print(df_th1_4_18.head())

# Plot all columns as time series.
df_th1_4_18.plot(subplots=True)
plt.suptitle("Columns theta1-theta4 in 2018 as time series ")
plt.show(block=False)

# Plot histograms of all columns
df_th1_4_18.hist()
plt.suptitle("Histograms of columns theta1-theta4 in 2018")
plt.show(block=False)

# Plot all on a single, faceted plot.
df_th1_4_18.plot()
plt.suptitle("Columns theta1-theta4 in 2018 on a single, faceted plot")
plt.show(block=False)

# Plot KDE-s (Kernel Denisty Estimators) for all columns.
df_th1_4_18.plot.density(subplots=True)
plt.suptitle("KDE-s for columns theta1-theta4 in 2018")
plt.show()
