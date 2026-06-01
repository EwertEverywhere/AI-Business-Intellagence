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

#plt.show()

# Erkennung einer Gruppe aufgrund von 2 Kriterien
# Die Voranalyse zeigt, dass die 'Gruppe A' auf Grundlage der Werte der Kriterien X3 und X4 eindeutig identifiziert werden kann.

df_identified = df.loc[(df.X3 <= 1.9) & (df.X4 <= 0.6)]
print('Correct: ', df_identified.Y.count(), '/50')


print(Gruppe_B_df.describe())
print(Gruppe_C_df.describe())

df_idetified_B = df.loc[(df.X1<=7.0) & (df.X2<=3.4) & (df.X3<=5.1) & (df.X4<=1.8)]
print('Correct: ',df_idetified_B.Y.count(),'/50')
#df_idetified_three






