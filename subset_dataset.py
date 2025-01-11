import pandas as pd
# Pierwsze n wierszy
TOP_LIMIT = 3000

# Obcinamy dataset do pierwszych TOP_LIMIT wierszy
data = pd.read_csv("recipes.csv")
subset = data.head(TOP_LIMIT)

# Zapisanie do pliku CSV
subset.to_csv("subset_recipes.csv", index=False)
