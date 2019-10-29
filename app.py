from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='supermarket_price_sharing'
        )
    return connection

@app.route("/")
def form():
   return render_template("index.template.html")


@app.route("/", methods=["POST"])
def submit_form():
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    username = request.form["username"]
    supermarket = request.form["supermarket"]
    location = request.form["location"]
    address = request.form["address"]
    brand = request.form["brand"]
    item = request.form["item"]
    itemcost = request.form["price"]
    
    #username insertion to database
    sql = """
         INSERT INTO user(id, username)
         VALUES (NULL, "{}")
        """.format(username)
    
    cursor.execute(sql)
    connection.commit()
    
    
    #search and select user_id
    
    SQL_SEARCH_USER_ID="""
    SELECT id FROM user WHERE username="{}"
    """.format(username)
    
    cursor.execute(SQL_SEARCH_USER_ID)
    user_id = cursor.fetchone()["id"] 
    
    #push id to existing itemcost table
    
    SQL_INSERT_USER_ID="""
    INSERT INTO itemcost(user_id) VALUES({})
    """.format(user_id)
    
    #supermarket insertion to database
    sql = """
         INSERT INTO supermarket(name)
         VALUES ("{}")
        """.format(supermarket)
    
    cursor.execute(sql)
    connection.commit()
    
    #search and select supermarket id
    
    SQL_SEARCH_SUPERMARKET_ID="""
    SELECT id FROM supermarket WHERE name="{}"
    """.format(supermarket)
    
    cursor.execute(SQL_SEARCH_SUPERMARKET_ID)
    supermarket_id = cursor.fetchone()["id"] 
    
    #location and address insertion to database
    sql = """
         INSERT INTO location(address,name)
         VALUES ("{}","{}")
        """.format(address,location)
    
    cursor.execute(sql)
    connection.commit()
    
    #find location_id
    SQL_FIND_LOCATION_ID="""
    SELECT id FROM location WHERE name="{}"
    """.format(location)
    
    cursor.execute(SQL_FIND_LOCATION_ID)
    location_id = cursor.fetchone()["id"]
    
    #insert into location_supermarket
    SQL_INSERT_LOCATION_SUPERMARKET_ID="""
    INSERT INTO location_supermarket (location_id, supermarket_id) VALUES ("{}","{}")
    """.format(location_id,supermarket_id)
    
    cursor.execute(SQL_INSERT_LOCATION_SUPERMARKET_ID)
    connection.commit()
    
    #item insertion to database
    SQL_SEARCH_BRAND_ID="""
    SELECT id FROM brand WHERE name="{}"
    """.format(brand)
    cursor.execute(SQL_SEARCH_BRAND_ID)
    brand_id = cursor.fetchone()["id"]
    
    SQL_INSERT_BRAND_ID="""
    INSERT INTO `item` (`id`, `brand_id`, `name`) VALUES (NULL,"{}","{}")
    """.format(brand_id, item) 
    print(SQL_INSERT_BRAND_ID)
    cursor.execute(SQL_INSERT_BRAND_ID)
    connection.commit()
    
    #insert ids to brand_supermarket
    SQL_INSERT_BRAND_SUPERMARKET_ID="""
    INSERT INTO brand_supermarket (brand_id, supermarket_id) VALUES ("{}","{}")
    """.format(brand_id, supermarket_id)
    cursor.execute(SQL_INSERT_BRAND_SUPERMARKET_ID)
    connection.commit()
    
    #find item_id
    SQL_SEARCH_ITEM_ID="""
    SELECT id FROM item WHERE name="{}"
    """.format(item)
    cursor.execute(SQL_SEARCH_ITEM_ID)
    item_id = cursor.fetchone()["id"] 
    
    #cost insertion to database
    sql = """
         INSERT INTO itemcost(id, date, cost, user_id, item_id, supermarket_id)
         VALUES (NULL, CURRENT_TIMESTAMP, "{}","{}","{}","{}")
        """.format(itemcost, user_id, item_id,supermarket_id)
    
    cursor.execute(sql)
    connection.commit()

    
    return render_template("thanks.template.html")
    
@app.route("/table")
def table():
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    
    #username retrieval from database
    sql = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        """
        
    cursor.execute(sql)
    return render_template("table.template.html",results=cursor)
    
#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)