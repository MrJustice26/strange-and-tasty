import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

def load_models_and_data():
    """
    Funkcja ładująca dane i modele.
    """
    # Wczytanie przepisów
    df = pd.read_csv("mixed_recipes.csv")
    recipe_ids = df["Unnamed: 0"].tolist()
    recipe_texts = df["NER"].tolist()

    # Model językowy
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    recipe_vectors = model.encode(recipe_texts)

    # Model NearestNeighbors
    nn_model = NearestNeighbors(n_neighbors=1, metric="cosine")
    nn_model.fit(recipe_vectors)

    return model, nn_model, recipe_ids, df

def find_recipe(user_ingredients, model, nn_model, recipe_ids, df, error_threshold=0.25):
    """
    Znajdź przepis na podstawie składników użytkownika.
    """
    user_vector = model.encode([user_ingredients])
    distances, indices = nn_model.kneighbors(user_vector)
    if distances[0][0] > error_threshold:
        return None

    closest_recipe_id = recipe_ids[indices[0][0]]
    recipe = df.iloc[closest_recipe_id]

    return {
        "id": int(recipe["Unnamed: 0"]),
        "title": recipe["title"],
        "ingredients": ", ".join(eval(recipe["ingredients"])),  # Zamiana tablicy na tekst
        "directions": " ".join(eval(recipe["directions"])),     # Zamiana tablicy na tekst
        "link": recipe.get("link", ""),
        "source": recipe.get("source", "Unknown"),
        "NER": ", ".join(eval(recipe["NER"]))                  # Zamiana tablicy na tekst
    }