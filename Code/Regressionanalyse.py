# laden der Bibliotheken
# python -m pip install numpy
import numpy as np # Bibliothek zum Ausführen der statistischen und mathematischen Operationen.
# python -m pip install pandas
import pandas as pd # Bibliothek für auslesen der Daten aus Dateien der verschiedenen Formate und bilden der Datenstrukturen. 
# python -m pip install scikit-learn
from sklearn.preprocessing import StandardScaler # ???
scale = StandardScaler()

# lese den Datensatz
df = pd.read_csv("../datasets/data_six.csv")

#print(df.head())
#print(df.describe())

# z-Transformation der ersten unabhängigen Varialble

# - erste variable auswählen
x = df.iloc[:,[0]]

print(x.describe())

# transformiertn der wahriable

scaled_x = scale.fit_transform(x)

mean_scaled = np.mean(scaled_x)

mean_scaled = round(mean_scaled)

print(mean_scaled)

# alle 3 variablen weisen unterschiedliche Mittelwerte und standardabweichungen aus. Die situation führt dazu, dass die Mittelwerte der einzelnen Variablen nicht direkt mit einander vergleichbar sind.
# eine normalisierung setzt alle Werte auf 0 und ermöglicht damit eine direkte vergleichbarkeit der Werte mit einander.


std_scaled = np.std(scaled_x)
std_scaled = round(std_scaled)

print(std_scaled)

#
