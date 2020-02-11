import datetime as dt
import numpy as np
import sqlalchemy
import scrape_emojis
import scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

#### Setup Flask ####
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/emojis")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_data = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_everything()

    # Delete everything
    mongo.db.mars.drop()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.insert(mars_data)

    # Redirect back to home page
    return redirect("/")

# Route that will trigger the scrape function
@app.route("/emojis")
def emojis():

    # Run the scrape function
    data = scrape_emojis.get_emojis()

    # Delete everything
    mongo.db.emojis.drop()

    # Update the Mongo database using update and upsert=True
    mongo.db.emojis.insert_many(data)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
