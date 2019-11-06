from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql
import urllib.parse
from urllib.parse import urlparse

urllib.parse.uses_netloc.append('mysql')


app = Flask(__name__)

def get_connection():
    
    # url = urlparse(os.environ['CLEARDB_DATABASE_URL'])
    # name = url.path[1:]
    # user = url.username
    # password= url.password
    # host = url.hostname
    # port= url.port

    
    # connection = pymysql.connect(
    #     host=host,
    #     user=user,
    #     password=password,
    #     port=port,
    #     database=name
    #     )
        
    connection = pymysql.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASSWORD'),
        database=os.getenv('SQL_DATABASE')
        )	        
    return connection

@app.route("/")
def homepage():
    return render_template("index.template.html")

@app.route("/submit")
def form():
   return render_template("form.template.html")


@app.route("/submit", methods=["POST"])
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
    SELECT * FROM user ORDER BY id DESC LIMIT 1
    """
    
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
    SELECT * FROM supermarket ORDER BY id DESC LIMIT 1
    """
    
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
    
@app.route("/edit/<itemcost_id>")
def edit(itemcost_id):
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    
    #username retrieval from database
    sql = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        WHERE itemcost.id="{}"
        """.format(itemcost_id)
        
    cursor.execute(sql)
    return render_template("edit.template.html",results=cursor)
    
@app.route("/edit/<itemcost_id>", methods=["POST"])
def submit_edit(itemcost_id):
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    supermarket = request.form["supermarket"]
    itemcost = request.form["price"]
    username = request.form["username"]
    
    SQL_UPDATE_USERNAME = """
    UPDATE `itemcost` 
    INNER JOIN user ON itemcost.user_id=user.id 
    SET user.username="{}" WHERE itemcost.id="{}"
    """.format(username, itemcost_id)
    
    cursor.execute(SQL_UPDATE_USERNAME)
    connection.commit()
    
    
    SQL_UPDATE_SUPERMARKET = """
    UPDATE `itemcost` 
    INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id 
    SET supermarket.name="{}" WHERE itemcost.id="{}"
    """.format(supermarket, itemcost_id)
    
    cursor.execute(SQL_UPDATE_SUPERMARKET)
    connection.commit()
    
    
    SQL_UPDATE_COST = """
    UPDATE `itemcost`SET cost="{}" WHERE itemcost.id="{}"
    """.format(itemcost, itemcost_id)
    
    cursor.execute(SQL_UPDATE_COST)
    connection.commit()
    connection.close()
    
    return table()


@app.route("/delete/<itemcost_id>")
def delete_confirmation(itemcost_id):
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    
    #username retrieval from database
    sql = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        WHERE itemcost.id="{}"
        """.format(itemcost_id)
        
    cursor.execute(sql)
    return render_template("delete.template.html",results=cursor)
    
@app.route("/delete/<itemcost_id>", methods=["POST"])
def delete_confirmed(itemcost_id):
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    #delete location_supermarket relation
    #search supermarket id
    SQL_SELECT_SUPERMARKET_ID="""
    SELECT supermarket_id FROM itemcost INNER JOIN supermarket 
    ON itemcost.supermarket_id=supermarket.id 
    WHERE itemcost.id="{}"
    """.format(itemcost_id)
    
    cursor.execute(SQL_SELECT_SUPERMARKET_ID)
    supermarket_id = cursor.fetchone()["supermarket_id"]
    print("Look here: ")
    print(supermarket_id)
    #select location_supermarket id's
    
    SQL_SELECT_LOCATION_SUPERMARKET_ID="""
    SELECT location_id, supermarket_id FROM location_supermarket WHERE supermarket_id="{}"
    """.format(supermarket_id)
    
    cursor.execute(SQL_SELECT_LOCATION_SUPERMARKET_ID)
    
    #deleting relation
    SQL_DELETE_LOCATION_SUPERMARKET_RELATION="""
    DELETE FROM location_supermarket WHERE supermarket_id="{}"
    """.format(supermarket_id)
    
    cursor.execute(SQL_DELETE_LOCATION_SUPERMARKET_RELATION)
    connection.commit()
    
    SQL_DELETE_BRAND_SUPERMARKET_RELATION="""
    DELETE FROM brand_supermarket WHERE supermarket_id="{}"
    """.format(supermarket_id)
    
    cursor.execute(SQL_DELETE_BRAND_SUPERMARKET_RELATION)
    connection.commit()
    
    #delete location
    SQL_DELETE_LOCATION="""
    DELETE FROM location WHERE ID="{}"
    """.format(supermarket_id)
    
    cursor.execute(SQL_DELETE_LOCATION)
    connection.commit()
    
    #delete supermarket
    SQL_DELETE_SUPERMARKET="""
    DELETE FROM supermarket WHERE id="{}"
    """.format(supermarket_id)
    
    cursor.execute(SQL_DELETE_SUPERMARKET)
    connection.commit()
    
    #delete item
    SQL_DELETE_ITEM="""
    DELETE FROM item WHERE id="{}"
    """.format(itemcost_id)
    
    cursor.execute(SQL_DELETE_ITEM)
    connection.commit()
    
    #delete user
    SQL_DELETE_USER="""
    DELETE FROM user WHERE id="{}"
    """.format(itemcost_id)
    
    cursor.execute(SQL_DELETE_USER)
    connection.commit()
    
    return table()
    
@app.route("/search")
def search_page():
    return render_template("search.template.html")
    
@app.route("/search", methods=["POST"])
def search():
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    search_term = request.form["search-bar"]
    search_input = request.form["search-input"]
    
    if search_term == "1":
        SQL_SEARCH_BY_ITEM = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        WHERE item.name="{}"
        """.format(search_input)
        
        cursor.execute(SQL_SEARCH_BY_ITEM)
        return render_template("search.template.html", results=cursor)
        
    elif search_term == "2":
        SQL_SEARCH_BY_SUPERMARKET = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        WHERE supermarket.name="{}"
        """.format(search_input)
        
        cursor.execute(SQL_SEARCH_BY_SUPERMARKET)
        return render_template("search.template.html", results=cursor)
    
    else:
        SQL_SEARCH_BY_USER = """
        SELECT itemcost.id, itemcost.date, itemcost.cost, item.name, supermarket.name, user.username  FROM `itemcost` 
        INNER JOIN user ON itemcost.user_id=user.id
        INNER JOIN item ON itemcost.item_id=item.id
        INNER JOIN supermarket ON itemcost.supermarket_id=supermarket.id
        WHERE user.username="{}"
        """.format(search_input)
        
        cursor.execute(SQL_SEARCH_BY_USER)
        return render_template("search.template.html", results=cursor)
    
    
    # return render_template("search.template.html")    



#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)