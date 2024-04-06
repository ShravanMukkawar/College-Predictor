import secrets;
from app import app;
from .rvp import pvr;
from .algo import finalList;

from flask import render_template, request, redirect, flash

@app.route("/")
def new():
    return render_template("base.html")

@app.route("/getcollege", methods=[ 'GET','POST'])
def getcollege():
    if request.method == 'POST':
        college_name = request.form['college']
        colleges = ["coep", "vjti", "pict","ict"]
        if college_name in colleges:
            return render_template(f"{college_name}.html")
        else:
            return "College not found!"

@app.route("/index",  methods=["GET","POST"])
def index():

    secret_key=secrets.token_hex(16)
    app.config["SECRET_KEY"] = secret_key

    if(request.method == "POST"):
        req = request.form
        rank = req["rank"]
        state = req["state"]
        pwd = req["pwd"]
        gender = req["gender"]
        category = req["category"]

    
        if(rank == ""):
            flash("Please enter either your Rank or your Percentile",'error')
            return redirect(request.url)
        
        if(rank == ""):
            ranks = pvr(pwd,category)
            ranks = int(ranks)

            if(ranks <= 0):
                ranks = 2
            result = finalList(ranks,category,state,gender,pwd)

        if(rank):
            result = finalList(int(rank),category,state,gender,pwd)
            ranks = rank
        

        return render_template("result.html",ranks=ranks,category=category,tables=[result.to_html(classes='data')], titles=result.columns.values)

    return render_template("index.html")

@app.route("/exams")
def exams():
    return render_template("exams.html")

