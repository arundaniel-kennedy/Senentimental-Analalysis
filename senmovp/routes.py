from flask import Flask,render_template,request
import mysql.connector
import json

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'movie',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

mycursor = link.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM movies order by year desc limit 5")
    myresult = mycursor.fetchall()

    return render_template("index.html",result=myresult)

@app.route('/browse')
def browse():
    mycursor.execute("SELECT * FROM movies limit 50")
    myresult = mycursor.fetchall()

    return render_template("cards.html",result=myresult)

@app.route('/search/<name>')
def searchbox(name):
    mycursor.execute("SELECT id,title FROM movies where title like '"+name+"%' limit 20")
    myresult = mycursor.fetchall()

    return render_template("search.html",result=myresult)

@app.route('/result',methods=['POST'])
def search():
    name = request.form['name']
    name = name.split('(')
    id = name[-1].split(')')

    #return str(id[0])

    mycursor.execute("SELECT comment FROM movies WHERE id = '"+id[0]+"'")
    comment = mycursor.fetchall()

    sum=0
    comments=[]

    data = json.loads(comment[0][0])
    for c in data:
        mycursor.execute("SELECT id FROM review WHERE slno = '"+str(c)+"'")
        comment = mycursor.fetchone()
        sum+=int(comment[0])
        mycursor.execute("SELECT comment FROM review WHERE slno = '"+str(c)+"'")
        comme = mycursor.fetchone()
        comments.append(comme[0])

    avg = (sum/20)*100

    mycursor.execute("SELECT * FROM movies WHERE id = '"+id[0]+"'")
    myresult = mycursor.fetchone()

    return render_template("contentpage.html",x=myresult,rate=format(round(avg,2)),comments=comments)

@app.route('/genres')
def genres():
    mycursor.execute("SELECT * FROM genre")
    myresult = mycursor.fetchall()
    return render_template("genre.html",result=myresult)

@app.route('/genre/<id>')
def genre(id):
    mycursor.execute("SELECT * FROM movies")
    myresult = mycursor.fetchall()
    ch=[]
    for i in myresult:
        if(id in i[12]):
            ch.append(i)
    return render_template("cards.html",result=ch)


@app.route('/highrate')
def highrate():
    mycursor.execute("SELECT * FROM movies order by vote_average desc limit 50")
    myresult = mycursor.fetchall()

    return render_template("cards.html",result=myresult)

@app.route('/alphabet')
def alpha():
    mycursor.execute("SELECT * FROM movies order by title limit 50")
    myresult = mycursor.fetchall()

    return render_template("cards.html",result=myresult)

@app.route('/year')
def year():
    mycursor.execute("SELECT * FROM movies order by year desc limit 50")
    myresult = mycursor.fetchall()

    return render_template("cards.html",result=myresult)

@app.route('/content/<id>')
def contentpage(id):
    mycursor.execute("SELECT comment FROM movies WHERE id = '"+id+"'")
    comment = mycursor.fetchall()

    sum=0
    comments=[]

    data = json.loads(comment[0][0])
    for c in data:
        mycursor.execute("SELECT id FROM review WHERE slno = '"+str(c)+"'")
        comment = mycursor.fetchone()
        sum+=int(comment[0])
        mycursor.execute("SELECT comment FROM review WHERE slno = '"+str(c)+"'")
        comme = mycursor.fetchone()
        comments.append(comme[0])

    avg = (sum/20)*100

    mycursor.execute("SELECT * FROM movies WHERE id = '"+id+"'")
    myresult = mycursor.fetchone()

    return render_template("contentpage.html",x=myresult,rate=format(round(avg,2)),comments=comments)


if __name__ == "__main__":
    app.run(debug=True)
