import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import array


a = np.array([41,45,43,38,36,38,40,39])

a = pd.DataFrame(
                    {
                        'Values':a,
                        'ID':[1,2,3,4,5,6,7,8]
                    }
                )


a = a.sort_values(by='Values')

mean = a['Values'].mean()
mode = a['Values'].mode()
median = a['Values'].median()



print('Häufigster Wert '  + str(mode) + 'Mittelwert ' + str(mean) + 'Median ' + str(median))


# definiere Mittelwert und normalverteilung

avarage = 40
std_dev = 5

# erstelle die Array

nuberes = np.random.normal(loc=avarage, scale=std_dev, size=1000)
nuberes = np.round(nuberes)

nuberes = np.clip(nuberes,30,50)

# statistic ausrechnen

# mittelwert
mittelwert = np.mean(nuberes)

# variance
variance = np.var(nuberes)


print(variance)
