import pandas as pd

csv1 = pd.read_csv('subset_recipes.csv')
csv2 = pd.read_csv('strange_recipes.csv')

csv2['Unnamed: 0'] = csv2['Unnamed: 0'].apply(lambda x: int(x) + 3000)

polaczone = pd.concat([csv1, csv2], ignore_index=True)

polaczone.to_csv('polaczone.csv', index=False)

print("Pliki zostały połączone i dodano kolumnę z oryginalnym indeksem!")
