import mysql.connector
 
class MySQLPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host='database',  # ou 'db' si vous utilisez Docker Compose
            user='root',
            password='root',
            database='price_comparator'
        )
        self.cursor = self.connection.cursor()
 
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
 
    def process_item(self, item, spider):
        # Insérer dans la base de données
        self.cursor.execute("""
            INSERT INTO products (name, price, link, image, site)
            VALUES (%s, %s, %s, %s, %s)
        """, (item['name'], item['price'], item['link'], item['image'], item['site']))
        self.connection.commit()
        return item