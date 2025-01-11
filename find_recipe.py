import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

ERROR_THRESHOLD = 0.25

# Wczytanie przepisów z pliku CSV
df = pd.read_csv("subset_recipes.csv")  # Wczytaj plik CSV
recipe_ids = df["Unnamed: 0"].tolist()  # Pobranie ID przepisów
recipe_texts = df["NER"].tolist()  # Pobranie listy składników

# Model językowy
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Sentence-BERT

# Zamiana składników na wektory
recipe_vectors = model.encode(recipe_texts)  # Zamiana składników na wektory liczbowe

# Tworzenie modelu NearestNeighbors
nn_model = NearestNeighbors(n_neighbors=1, metric="cosine")  # Model wyszukiwania najbliższych sąsiadów
nn_model.fit(recipe_vectors)  # Dopasowanie wektorów przepisów

# Obsługa zapytania użytkownika
def find_recipe(user_ingredients, error_threshold=ERROR_THRESHOLD):
    """
    Znajdź przepis na podstawie składników użytkownika.
    """

    # Zamiana składników użytkownika na wektor
    user_vector = model.encode([user_ingredients])

    # Wyszukiwanie najbardziej podobnego przepisu
    distances, indices = nn_model.kneighbors(user_vector)
    print(distances)
    if distances[0][0] > error_threshold:
        return None

    # Pobranie ID najlepiej dopasowanego przepisu
    closest_recipe_id = recipe_ids[indices[0][0]]
    return df.iloc[closest_recipe_id]


print(find_recipe("cheese, butter, garlic powder, salt", error_threshold=0.4))