from flask import Flask,render_template,request,redirect,url_for
from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
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

mycursor = link.cursor()

def similar(id):
    mov=[]

def com(comment):
    totneg=0
    totpos=0

    porter = PorterStemmer()
    lancaster = LancasterStemmer()

    stopfile = open("stopwords.txt",'r')
    stopwords = stopfile.read()
    stopwords = stopwords.split()

    negfile = open("negative-words.txt",'r', encoding = "ISO-8859-1")
    negwords = negfile.read()
    negwords = negwords.split()

    posfile = open("positive-words.txt",'r', encoding = "ISO-8859-1")
    poswords = posfile.read()
    poswords = poswords.split()

    #comment ="it sends you away a believer again and quite cheered at just that"

    exclude = set(string.punctuation)
    comment = ''.join(ch for ch in comment if ch not in exclude)
    comment = comment.split()


    x =' '.join( j for j in comment if j not in stopwords)
    x = x.split()

    for j in x:
        if j in negwords:
            totneg+=1

    for j in x:
        if j in poswords:
            totpos+=1

    #print(totneg,totpos)
    if(totneg>totpos):
        return("0")
    elif(totneg<totpos):
        return("1")
    else:
        return("0")

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

@app.route('/content/<id>')
def contentpage(id):

    #simmov = similar(id)

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

    return render_template("contentpage.html",x=myresult,rate=format(round(avg,2)),comments=comments)

@app.route('/comment',methods=['POST'])
def addcomments():
    comment = request.form['comment']
    id = request.form['id']

    comval = com(comment)

    mycursor.execute("SELECT * FROM review")
    myresult = mycursor.fetchall()

    slno = mycursor.rowcount

    mycursor.execute("INSERT INTO `review` (`slno`, `id`, `comment`) VALUES (NULL,'"+comval+"', '"+comment+"')")
    link.commit()

    mycursor.execute("SELECT comment FROM movies WHERE id = '"+id+"'")
    comment = mycursor.fetchall()

    comments=[]

    data = json.loads(comment[0][0])

    data.append(slno)

    mycursor.execute("UPDATE `movies` SET `comment` = '"+str(data)+"' WHERE `id` = '"+str(id)+"'")
    link.commit()

    return redirect(url_for('contentpage',id=id))

if __name__ == "__main__":
    app.run(debug=True)
