from flask import Flask,render_template,request,redirect,url_for,session
import pandas as pd
import joblib
import re
from nltk.corpus import stopwords
import string
import mysql.connector
import json

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'movie',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

mycursor = link.cursor(buffered=True)

forest = joblib.load('forest.pkl')
vectorizer = joblib.load('bow.pkl')

sim=pd.read_csv("t2.csv")

def similar(id):
    mycursor.execute("SELECT title FROM movies where id='"+str(id)+"'")
    name = mycursor.fetchone()
    name = name[0]

    def srt(s):
      return s[1]

    #name = 'Avatar (2009 film)'
    s=sim[name].sum()
    d=[]
    for i in sim.columns[1:]:
      sm=(sim[name]*sim[i]).sum()/s
      d.append([i.replace(' ',' '),sm])
    d=sorted(d,key=srt,reverse=True)
    d= [item for sublist in d for item in sublist]
    #k=d.find(0)
    #for i in d[:19:2]:

    return d

def com(comment):
    def reviewWords(review):
        data_train_num = re.sub(r'[0-9]+', 'number', review)  # Converting numbers to "NUMBER"
        data_train_lower = review.lower()              # Converting to lower case.
        data_train_split = data_train_lower.split()            # Splitting into individual words.
        stopWords = set(stopwords.words("english") )
        meaningful_words = [w for w in data_train_split if not w in stopWords]     # Removing stop words.
        return( " ".join( meaningful_words ))

    cleanWords=[]
    #comment='entertainment more disposable than hanna-barberas half-hour cartoons ever were'
    cleanWords.append(reviewWords(comment))
    data_test_features = vectorizer.transform(cleanWords)
    result = forest.predict(data_test_features)

    return(str(result[0]))

app = Flask(__name__)
app.secret_key = "3d6f45a5fc12445dbac2f59c3b6c7cb1"

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

    return contentpage(id[0])

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

@app.route('/similar/<id>')
def simi(id):
    simmov = similar(id)
    f = []

    for i in range(0,100,2):
        mycursor.execute('SELECT * FROM movies where title="'+str(simmov[i])+'"')
        myresult = mycursor.fetchone()
        print(myresult, str(simmov[i]))
        myresult = list(myresult)
        myresult.append(simmov[i+1])
        #print(myresult)
        f.append(tuple(myresult))


    return render_template("cards2.html",result=f)

@app.route('/content/<id>')
def contentpage(id):

    simmov = similar(id)

    mycursor.execute("SELECT comment FROM movies WHERE id = '"+id+"'")
    comment = mycursor.fetchall()

    sum=0
    comments=[]

    data = json.loads(comment[0][0])
    si = len(data)

    for c in data:
        mycursor.execute("SELECT id,comment FROM review WHERE slno = '"+str(c)+"'")
        comment = mycursor.fetchone()
        sum+=int(comment[0])
        comments.append(comment[1])

    avg = (sum/si)*100

    mycursor.execute("SELECT * FROM movies WHERE id = '"+id+"'")
    myresult = mycursor.fetchone()

    f=[]
    for i in range(0,10,2):

        mycursor.execute('SELECT * FROM movies where title="'+simmov[i]+'"')
        myresult1 = mycursor.fetchall()
        #print(myresult1)
        f.append(myresult1)
    f.pop(0)
    return render_template("contentpage.html",x=myresult,rate=format(round(avg,2)),comments=comments,simmov=f)

@app.route('/comment',methods=['POST'])
def addcomments():
    comment = request.form['comment']
    id = request.form['id']

    comval = com(comment)

    mycursor.execute("INSERT INTO `review` (`slno`, `id`, `comment`) VALUES (NULL,'"+comval+"', '"+comment+"')")
    link.commit()

    mycursor.execute("SELECT * FROM review")
    myresult = mycursor.fetchall()

    slno = mycursor.rowcount

    mycursor.execute("SELECT comment FROM movies WHERE id = '"+id+"'")
    comment = mycursor.fetchall()

    comments=[]

    data = json.loads(comment[0][0])

    data.append(slno)

    mycursor.execute("UPDATE `movies` SET `comment` = '"+str(data)+"' WHERE `id` = '"+str(id)+"'")
    link.commit()

    return redirect(url_for('contentpage',id=id))

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    id = request.form['id']

    mycursor.execute('SELECT * FROM login WHERE username = "'+username+'" and password="'+password+'"')
    comment = mycursor.fetchall()

    if mycursor.rowcount == 1:
        session['username']=username

    return redirect(url_for('contentpage',id=id))

if __name__ == "__main__":
    app.run(host='192.168.1.4', port=40974, debug=True)
