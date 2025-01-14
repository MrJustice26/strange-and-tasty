from backend.find_recipe import load_models_and_data,find_recipe

arguments = []
responses = []
print("Loading models and data...")
model, nn_model, recipe_ids, df = load_models_and_data()
print("Loaded")
while True:
    ingredients = input("ingredients: ")
    if ingredients == '':
        break
    threshold = input("threshold: ")
    safe_threshold = float(threshold) if threshold else 0.30
    print(f'DEBUG: ingredients: {ingredients}, threshold: {str(safe_threshold)}')
    response = find_recipe(ingredients, model, nn_model, recipe_ids, df, error_threshold=safe_threshold)
    print(response)
    if response:
        response = str(response["id"])
    else:
        response = "None"
    is_satisfied = input("satisfied?: ")
    ingredients_to_save = f'{str(safe_threshold)},"{ingredients}"'
    arguments.append(ingredients_to_save)
    print(f"DEBUG: Arguments: {ingredients_to_save} saved")
    if not is_satisfied:
        desired_response_id = input("What id then?: ")
        response = desired_response_id
    print(f"DEBUG: Response: {response} saved")
    responses.append(response)

str_responses = "\n".join(responses)
str_arguments = "\n".join(arguments)
with open("./test/in.csv", "w", encoding="utf-8") as inf, open("./test/out.csv", "w", encoding="utf-8") as outf:
    outf.write(str_responses)
    inf.write(str_arguments)