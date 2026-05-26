# Importiere alle relevante Bibliotheken

# Die relevanten Bibliotheken sind:
# Panda ist die Bibliothek um die dataen aus der Dateien verschiedene Formate zu laden um zu transformieren.
# Numpy ist die Bibliothek um die berechnungen durchzuführen.
# sklearn ist die Bibliotheck mit statistischen funktionen
# matplot ist die bibliotheck um die visuelle darstellungen zu machen. Aus matplotlib muss explizit pyplot geladen werden.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
model = LinearRegression()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# Lade die daten: aus der csv datei data_six.csv

df = pd.read_csv("../datasets/data_six.csv")

#print(df.describe())

col = df.iloc[:,[0]]
#print (col.describe())
col_trans = scaler.fit_transform(col)
#print(round(col_trans.mean()))

# Bivariate analyse

print(df.corr())

#df.boxplot()
#plt.show()


# multivariate analyses

Y = df.iloc[:,[2]]
X = df.iloc[:,[0,1]]

reg = model.fit(X,Y)

print(model.intercept_)
print(model.coef_)

plt.scatter(df.Y, df.X1)

plt.show()