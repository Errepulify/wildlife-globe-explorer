import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wildlife_globe'
app.config["MONGO_URI"] = 'mongodb+srv://User63:admin3Lobe90@myfirstcluster-maf2n.mongodb.net/wildlife_globe?retryWrites=true'

mongo = PyMongo(app)

 #Pulls data entered to be shown in spotlist.html#
@app.route('/spotlist_list')
def get_spot():
     return render_template("spotlist.html", 
                           spotlists=mongo.db.spotlist.find())

#To make the link Home work and redirect back to index.html#
@app.route('/')  
@app.route('/go_home')
def go_home():
    return render_template("index.html")


#To make the link spotlist work and redirect back to spotlist.html#
@app.route('/spotlist_list')
def spotlist_list():
    return render_template("spotlist.html")

#to make the link add spot work and redirect back to the addspot.html*
@app.route('/add_spot')
def add_spot():
    return render_template("addspot.html")
    

#What user typed in form is send to the database#    
@app.route('/insert_spot', methods=['POST'])
def insert_spot():
    spotlist =  mongo.db.spotlist
    spotlist.insert_one(request.form.to_dict())
    return redirect(url_for('spotlist_list'))
    
                           
                          
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)