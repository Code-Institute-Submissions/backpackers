from flask import Flask,render_template,request,redirect
import os
from flask_pymongo import PyMongo
from flask_mail import Mail
from flask_mail import Message
from bson.objectid import ObjectId
from base64 import b64encode
import base64
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')

mail = Mail(app)
mongo = PyMongo(app)


county_names = ["Antrim","Armagh","Carlow","Cavan","Clare","Cork","Derry","Donegal","Down","Dublin","Fermanagh","Galway","Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Tyrone","Waterford","Westmeath","Wexford","Wicklow"]


@app.route('/')
def home():
        if "county" in request.args:
            
            tasks=mongo.db.spots.find({"county": request.args["county"] })
        else:
            tasks = mongo.db.spots.find()
        return render_template("index.html",tasks=tasks,county_names=county_names)
        
        
@app.route('/find_spot',methods=["GET","POST"])    
def find():
    if request.method=="POST":
        if "county" or "spot_name" or "spot_place" or "rating" in request.form:
            print(request.form["spot_place"]);
            
            tasks=mongo.db.spots.find({"county": request.form["county"], "spot_name": {'$regex': request.form["spot_name"].capitalize()},"spot_place" :request.form["spot_place"]})
            # tasks=mongo.db.spots.find({"county": request.form["county"],"spot_name": {'$regex': request.form["spot_name"].capitalize()},"spot_place":request.form["spot_place"],"rating":request.form["rating"]})
        else:
            tasks = mongo.db.spots.find()
        return render_template("index.html",tasks=tasks,county_names=county_names)
        
    else:
        todo=mongo.db.things_to_do.find()
        return render_template("find.html", county_names=county_names,todo=todo)
    
        
@app.route('/add_spot',methods=["GET","POST"])
def add():
    if request.method=="POST":
        
        form_values = request.form.to_dict()
        if "image" in request.files:
            image = request.files['image']  
            image_string = base64.b64encode(image.read()).decode("utf-8")
            form_values["image"] = "data:image/png;base64," + image_string
        form_values["things_todo"]=request.form.getlist('things_todo')
        print(form_values)
        mongo.db.spots.insert_one(form_values)
        msg = Message("Spot Adding",
                  sender="backpackerssite1@gmail.com",
                  recipients=[form_values["email"]])
        msg.body="Thank you for adding the spot in backpackers site"
        mail.send(msg)
    
        return redirect("/")
        
    else:
        # county=mongo.db.county.find()
        todo=mongo.db.things_to_do.find()
        return render_template("add.html", county_names=county_names,todo=todo)
@app.route('/edit/<spot>/<spot_id>',methods=["GET","POST"])
def edit(spot,spot_id):
    if request.method=="POST":
        form_values = request.form.to_dict()
        if "image" in request.files:
            image = request.files['image']  
            image_string = base64.b64encode(image.read()).decode("utf-8")
            form_values["image"] = "data:image/png;base64," + image_string
           
        else:
            old_spot = mongo.db['spots'].find_one({"_id": ObjectId(spot_id)})
            form_values['image'] = old_spot['image']
            form_values["things_todo"]=request.form.getlist('things_todo') 
        mongo.db[spot].update({"_id": ObjectId(spot_id)}, form_values)
        return redirect("/")
        
    else:
        todo=mongo.db.things_to_do.find()
        the_spot =  mongo.db["spots"].find_one({"_id": ObjectId(spot_id)})
        return render_template('edit.html', the_spot=the_spot,county_names=county_names,todo=todo)
        
@app.route("/")
def index():

    msg = Message("Hello",
                  sender="backpackerssite1@gmail.com",
                  recipients=["femystephen16@gmail.com"])
    mail.send(msg)
    return redirect("/")
        

    
if __name__ == "__main__":
       app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)


    
    
 