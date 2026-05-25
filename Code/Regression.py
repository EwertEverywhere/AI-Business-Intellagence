# python -m pip install pandas
import pandas as pd
# python -m pip install numpy
import numpy as np
# python -m pip install matplotlib
import matplotlib.pyplot as plt
# python -m pip install scikit-learn
from sklearn.linear_model import LinearRegression


# Y - volumen der Baumstämme
# x1 - Umfang eines Baumstammes 
# X2 - Höhe eines Baumstammes

df = pd.read_csv("../datasets/data_six.csv")

print(df.describe())


# Univariate Statistik Plasiprüfung

# plot the results as boxplot
#df.boxplot()
#title_boxplot='Descreptive Statistic'
#plt.title(title_boxplot)

#plt.show()

# Bivarvariate Statistik
# kovarianz
print(df.corr())

#plt.scatter(df.Y,df.X1)
#plt.show()

# Multivariate Correlation

Y = df.iloc[:,2]
X = df.iloc[:,[0,1]]

print(X.describe())

model = LinearRegression()
model.fit(X,Y)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(model.intercept_)
print(model.coef_)
print(model.score(X,Y))