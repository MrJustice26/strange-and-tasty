from flask import Flask, request, jsonify
from find_recipe import load_models_and_data, find_recipe

app = Flask(__name__)

# Ładowanie modeli przy starcie serwera
print("Loading models and data, please wait...")
model, nn_model, recipe_ids, df = load_models_and_data()
print("Models and data loaded successfully!")

@app.route('/', methods=['GET'])
def home():
    """
    Prosty endpoint testowy, aby sprawdzić, czy serwer działa.
    """
    return jsonify({"message": "Welcome to the Recipe Finder API! Use POST /find-recipe to find recipes."}), 200

@app.route('/find-recipe', methods=['POST'])
def get_recipe():
    """
    Endpoint do wyszukiwania przepisów na podstawie składników.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400

        user_ingredients = data.get("ingredients")
        error_threshold = data.get("error-threshold", 0.25)

        if not user_ingredients:
            return jsonify({"error": "Missing 'ingredients' parameter"}), 400

        recipe = find_recipe(user_ingredients, model, nn_model, recipe_ids, df, error_threshold)

        if recipe is None:
            return jsonify({"error": "No recipe found within the error threshold"}), 404

        return jsonify(recipe), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
