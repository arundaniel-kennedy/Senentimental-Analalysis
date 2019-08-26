from flask import Flask,render_template
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'movies',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

mycursor = link.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/highrate')
def highrate():
    mycursor.execute("SELECT * FROM ads order by imdb desc limit 50")
    myresult = mycursor.fetchall()

    return render_template("highrate.html",result=myresult)

@app.route('/alphabet')
def alpha():
    mycursor.execute("SELECT * FROM ads order by title limit 50")
    myresult = mycursor.fetchall()

    return render_template("alpha.html",result=myresult)

@app.route('/year')
def year():
    mycursor.execute("SELECT * FROM ads limit 50")
    myresult = mycursor.fetchall()

    return render_template("year.html",result=myresult)

@app.route('/content/<id>')
def contentpage(id):
    mycursor.execute("SELECT id FROM review ORDER BY RAND() limit 20")
    rate = mycursor.fetchall()

    sum=0
    for y in rate:
        sum+=y[0]

    avg = (sum/20)*100

    #mycursor.execute("UPDATE `ads` SET `rating` = '"+str(avg)+"' WHERE `ads`.`tid` = '"+id+"'")
    #link.commit()

    mycursor.execute("SELECT * FROM ads WHERE tid = '"+id+"'")
    myresult = mycursor.fetchone()
    return render_template("contentpage.html",x=myresult,rate=avg)


if __name__ == "__main__":
    app.run(debug=True)
