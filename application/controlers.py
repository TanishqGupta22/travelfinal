from flask import render_template,request,Flask
from flask import current_app as app
from application.models import *

b=dict()
b["in"]=False
a=0

@app.route("/home.html",methods=["GET"])
def f1():
    if request.method=="GET":
        return render_template("home.html")
@app.route("/login.html",methods=["GET","POST"])
def f3():
    if request.method=="GET" and b["in"]==False:
        print(b)
        return render_template("login.html")
    elif request.method=="GET" and b["in"]:
        print(b)
        return render_template("Profile.html",a=b)
    else:
        a=dict(request.form)
        for i in a:
            b[i]=a[i]
            
        if "login" in a:
            print(b,"hhh")
            user=db.session.query(User).filter(User.mail==b["mail"]).first()
            b["city"]=user.city
            b["district"]=user.district
            b["name1"]=user.fName
            b["name2"]=user.lName
            b["phoneno"]=user.phoneNo
            b["in"]=True
            return render_template("home.html",a=b) # loging part
        else:
            if "submit" in a:
                b["in"]=True
                user=User(phoneNo=b["phoneno"],fName=b["name1"],lName=b["name2"],mail=b["mail"],city=b["city"],district=b["district"],password=b["password"])
                db.session.add(user)
                db.session.commit()
                return render_template("home.html",a=b)
            return render_template("form.html",a=b)
@app.route("/about.html",methods=["GET","POST"])
def f4():
    if request.method=="GET":
        return render_template("about.html")
@app.route("/tours.html",methods=["GET","POST"])
def f5():
    if request.method=="GET":
        return render_template("tours.html")
    else:
        a=dict(request.form)
        tour=[]
        for i in a:
            print(i)
            x=Hotel.query.filter_by(destination=i).all()
            tour.extend(x)
            print(tour)
            
        return render_template("hotel.html",a=tour)
@app.route("/destination.html",methods=["GET","POST"])
def f6():
    if request.method=="GET":
        return render_template("destination.html")
@app.route("/hotel.html",methods=["GET","POST"])
def f7():
    if request.method=="GET":
        pass
@app.route("/payment.html",methods=["GET","POST"])
def f8():
    if request.method=="GET":
        return render_template("payment.html")