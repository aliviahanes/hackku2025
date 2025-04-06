from flask import Flask, render_template, request, jsonify
from gemini import Gemini
from recipelist import RecipeList

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/grocery")
def grocery():
    return render_template("grocery.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

# API endpoint to get recipes based on user input
@app.route("/api/get_recipes", methods=["POST"])
def get_recipes():
    data = request.json
    user_food = data.get("user_food", "")
    if not user_food:
        return jsonify({"error": "No food input provided"}), 400

    gemini = Gemini()
    recipe_list = RecipeList(gemini.cost_and_ing(user_food))
    recipes = recipe_list.get_recipes()  # Assuming this method exists in RecipeList

    return jsonify({"recipes": recipes})

# API endpoint to generate meal plans
@app.route("/api/generate_meal_plan", methods=["POST"])
def generate_meal_plan():
    data = request.json
    meal_per_week = data.get("meal_per_week", 7)

    from google import genai
    client = genai.Client(api_key="AIzaSyBvtJlqf84VgrmPnrY42sh5GIjniGAJ7dE")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"What are some good meal-prepping meals for {meal_per_week} days?"
    )

    return jsonify({"meal_plan": response.text})

# API endpoint to process meal lists
@app.route("/api/process_meals", methods=["POST"])
def process_meals():
    data = request.json
    breakfast = data.get("breakfast", [])
    lunch = data.get("lunch", [])
    dinner = data.get("dinner", [])

    # Combine all meals into one list
    all_meals = breakfast + lunch + dinner
    user_food = ", ".join(all_meals)

    # Process the meals using Gemini and RecipeList
    gemini = Gemini()
    recipe_list = RecipeList(gemini.cost_and_ing(user_food))
    recipes = recipe_list.get_recipes()  # Assuming this method exists in RecipeList

    return jsonify({"recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)
