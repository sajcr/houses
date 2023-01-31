from flask import Flask, render_template, request
import sqlite3
from cs50 import SQL
from datetime import datetime
import locale

app = Flask(__name__)

prepaid = SQL("sqlite:///../prices/data/prices.db")

locale.setlocale(locale.LC_ALL, '')

@app.route('/', methods=["GET", "POST"])
def home():
    
    postcode = ""
    
    try:
        postcode = request.form.get("postcode").upper()
    except:
        pass
    
    prices = prepaid.execute("SELECT * FROM prices WHERE postcode=? ORDER BY date DESC", postcode)
        
    for item in prices:
        item['price'] = locale.currency(int(item['price']), grouping=True)
    
    return render_template("layout.html", prices=prices)


