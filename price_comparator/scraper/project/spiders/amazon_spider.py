from flask import Flask, render_template
import mysql.connector
 
app = Flask(__name__)
 
def get_data():
    connection = mysql.connector.connect(
        host='database,  # ou 'db' pour Docker
        user='user',
        password='password',
        database='price_comparator'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products ORDER BY name, site")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
 
@app.route('/')
def index():
    products = get_data()
    return render_template('index.html', products=products)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)