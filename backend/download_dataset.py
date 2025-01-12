import pandas as pd
import kagglehub
# Pobranie datasetu z Kaggle
path = kagglehub.dataset_download("paultimothymooney/recipenlg")

# Odczyt pliku CSV z datasetu
# Ustal plik główny w pobranym katalogu, zazwyczaj nazywa się np. `recipes.csv`
file_path = f"{path}/RecipeNLG_dataset.csv"  # Zmień nazwę pliku na właściwą, jeśli inna

# Wczytaj dane za pomocą Pandas
data = pd.read_csv(file_path)
data.to_csv("recipes.csv", index=False)
