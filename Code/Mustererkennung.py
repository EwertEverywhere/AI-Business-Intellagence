# import all relevant bibliothecks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataset 4

df = pd.read_csv("../datasets/data_four.csv")

print(df.head())
print('+++++++++++++++++++++++++++++++++++++')
print(df.describe())
print('+++++++++++++++++++++++++++++++++++++')

#df.boxplot()
#plt.show()

# daten vorbereiten. Einzelne Kategorieen nebeneinander in den Boxploten anzeigen.

Gruppe_A_df = df.loc[(df.Y == 'A')]
Gruppe_B_df = df.loc[(df.Y == 'B')]
Gruppe_C_df = df.loc[(df.Y == 'C')]

# Boxplot für 3 Kategorien erstellen

plt.subplot(1,3,1)
Gruppe_A_df.boxplot()
plt.ylim(0,8)
title_plot = "Gruppe A"
plt.title(title_plot)

plt.subplot(1,3,2)
Gruppe_B_df.boxplot()
plt.ylim(0,8)
title_plot = "Gruppe B"
plt.title(title_plot)

plt.subplot(1,3,3)
Gruppe_C_df.boxplot()
plt.ylim(0,8)
title_plot = "Gruppe C"
plt.title(title_plot)

plt.show()