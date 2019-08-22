## Step 1 - Scraping
## Step 2 - MongoDB and Flask Application

# Import Dependencies 
from flask import Flask, redirect, render_template  
import pymongo
import scrape_mars
import time

# Create an instance of Flask app
app = Flask(__name__)

# Create connection with MongoDB
conn = 'mongodb://localhost:27017'

# Pass connection to mongo instance
client = pymongo.MongoClient(conn)

# Create mars_Data Database
db = client.mars_db

# Drops collection if available to remove duplicates
db.collection.drop()

# Create mars_Data collection
collection = db.mars

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def index(): 
        ######################
        #db.collection.drop()
        #news_dict = db.collection.find()
        #return render_template("index.html", news_dict = news_dict)


        mars_info = db.collection.find()
        for info in mars_info:
                #Return template and data
                return render_template("index.html", mars_info = info)


# Route that will trigger scrape function

@app.route("/scrape")
def scraper():
                
        ####################
        #news_dict = scrape_mars.scrape_mars_news()
        #db.collection.insert_one(news_dict)
        #########################

        #############
        # Run the scrape function
        mars_data = scrape_mars.scrape_info()
        
        # Update the Mongo database using update and upsert=True
        #db.collection.update({}, mars_data, upsert=True)
        db.collection.insert(mars_data)
        #############
        #return redirect("/", code = 302)
        return redirect("/")


if __name__ == "__main__": 

    app.run(debug= True)