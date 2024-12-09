from flask import Flask, render_template
import mysql.connector
 
app = Flask(__name__)
 
def get_products():
    conn = mysql.connector.connect(
        host="database",
        user="root",
        password="root",
        database="comparateur"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, price, link FROM products ORDER BY price ASC")
    products = cursor.fetchall()
    conn.close()
    return products
 
@app.route("/")
def index():
    products = get_products()
    return render_template("index.html", products=products)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)