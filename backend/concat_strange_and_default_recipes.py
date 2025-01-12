import pandas as pd

# Wczytanie danych z dwóch plików CSV
csv1 = pd.read_csv('subset_recipes.csv')
csv2 = pd.read_csv('strange_recipes.csv')

csv2['Unnamed: 0'] = csv2['Unnamed: 0'].apply(lambda x: int(x) + 3000)

# Połączenie danych (dodanie wierszy z csv2 pod wiersze z csv1)
polaczone = pd.concat([csv1, csv2], ignore_index=True)

# Zapis do nowego pliku CSV (opcjonalne)
polaczone.to_csv('polaczone.csv', index=False)

print("Pliki zostały połączone i dodano kolumnę z oryginalnym indeksem!")
