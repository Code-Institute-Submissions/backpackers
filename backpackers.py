from flask import Flask,render_template,request,redirect
import os
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')
def home():
    tasks = mongo.db.spots.find()
    return render_template("index.html",tasks=tasks)
@app.route('/add_spot',methods=["GET","POST"])
def add():
    if request.method=="POST":
        form_values = request.form.to_dict()
        
        
        mongo.db.spots.insert_one(form_values)
        return redirect("/")
        
    else:
        county=mongo.db.county.find()
        return render_template("add.html", county=county)
    
if __name__ == "__main__":
       app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)


    
    
 