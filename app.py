from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)
