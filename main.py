from flask import Flask, render_template, request
from werkzeug.utils import redirect
from file_proc import pievienot

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

@app.route("/postData", methods = ["POST", "GET"])
def postData():
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        vards = request.form.get("vards")
        uzvards = request.form.get("uzvards") 
        epasts = request.form.get("epasts")
        if request.form.get("atbilde") == None: 
            atbilde = "Nē"
        else:
            atbilde = "Jā"
        zina = request.form.get("zina").replace("\n", "")

        information = [vards, uzvards, epasts, atbilde, zina]
        pievienot(information)
            
        return redirect("/form")
    else:
        return "Kas te notiek?"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
