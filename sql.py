import sqlite3 
con = sqlite3.connect("food.db")
cur = con.cursor()

def listallOrders():
    