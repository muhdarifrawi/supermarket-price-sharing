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
    cursor = connection.cursor()
    username = request.form["username"]

    
    #username insertion to database
    sql = """
         INSERT INTO user(username)
         VALUES ("{}")
        """.format(username)
    
    cursor.execute(sql)
    connection.commit()
    
    return render_template("thanks.template.html")
    
#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)