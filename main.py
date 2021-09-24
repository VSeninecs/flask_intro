from flask import Flask, render_template, request, redirect
from file_proc import pievienot, lasit

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
    status = request.args.get('status')
    return render_template("form.html", veiksmigi = status)

@app.route("/postData", methods = ["POST", "GET"])
def postData():
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        vards = request.form.get("vards")
        uzvards = request.form.get("uzvards")
        epasts = request.form.get("epasts")
        # print(request.form.get("atbilde"))
        if request.form.get("atbilde") == None: 
            atbilde = "Nē"
        else:
            atbilde = "Jā"
        zina = request.form.get("zina").replace("\n", "")

        information = [vards, uzvards, epasts, atbilde, zina]
        pievienot(information)
            
        return redirect("/form?status=1")
    else:
        return "Kas te notiek?"

@app.route("/form_results")
def lasitDatus():
    rindinas = lasit()
    dati = []
    for rindina in rindinas:
        ieraksts = rindina.split("`")
        dati.append(ieraksts)
    return render_template("form_results.html", rindinas = dati)
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)


