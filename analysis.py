import pandas as pd

data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)

print("Продажі по містах (ТИМЧАСОВА ВЕРСІЯ !!!):")
print(df)
print("Середнє значення:", df["sales"].mean())
