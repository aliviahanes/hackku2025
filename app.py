from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/planner")
def planner():
    return render_template("planner.html")

if __name__ == '__main__':
    app.run(debug=True)
