from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/my_projects")
def my_projects():
    return render_template("my_projects.html")

@app.route("/form")
def form():
    return render_template("form.html")
    
@app.route("/form_results")
def form_results():
    return render_template("form_results.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
