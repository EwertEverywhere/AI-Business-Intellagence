import pandas as pd
# python -m pip install statsmodels
import statsmodels.api as sm

# Datensatz anlegen

starwars = pd.DataFrame(
    {
        'Nerd':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Fan':[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    }
)

# Features difinieren

x = sm.add_constant(starwars['Nerd'])
y = starwars['Fan']

# Logistische Regressionsmodell

logit_model = sm.Logit(y,x)
result = logit_model.fit()
print(result.summary())