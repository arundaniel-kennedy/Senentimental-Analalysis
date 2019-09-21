import pandas as pd
import mysql.connector
import json
import string

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'movie',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
mycursor = link.cursor()




'''
mycursor.execute("SELECT genre FROM movies")
genre = mycursor.fetchall()
m=1

for i in genre:
    for j in i:
        data = json.loads(j)
        if(data==[]):
            mycursor.execute("UPDATE `movies` SET `mgen` = '"+"unknown"+"' WHERE `slno` = '"+str(m)+"'")
            link.commit()
            m+=1
        else:
            mycursor.execute("SELECT name FROM genre WHERE id='"+str(data[0])+"'")
            k = mycursor.fetchone()
            mycursor.execute("UPDATE `movies` SET `mgen` = '"+str(k[0])+"' WHERE `slno` = '"+str(m)+"'")
            link.commit()
            m+=1

'''

'''#key add
keyword =  pd.read_csv('tmdb.csv')
j=list(keyword['keywords'])

mycursor.execute("SELECT slno FROM movies")
k = mycursor.fetchall()

for i,f in zip(j,k):
    data = json.loads(i)
    lit=[]
    for element in data:
        for x,y in element.items():
            if(isinstance(y,int)):
                lit.append(y)
    mycursor.execute("UPDATE `movies` SET `keywords` = '"+str(lit)+"' WHERE `slno` = '"+str(f[0])+"'")
    link.commit()
'''
'''#genre add
genre=  pd.read_csv('tmdb.csv')
j=list(genre['genres'])

mars=''
mycursor.execute("SELECT slno FROM movies")
k = mycursor.fetchall()


for i,f in zip(j,k):
    data = json.loads(i)
    lit=[]
    for element in data:
        for x,y in element.items():
            if(isinstance(y,int)):
                lit.append(y)
    mycursor.execute("UPDATE `movies` SET `genre` = '"+str(lit)+"' WHERE `slno` = '"+str(f[0])+"'")
    link.commit()
                    #print(y)
'''

'''#add comments
mycursor.execute("SELECT slno FROM movies")
k = mycursor.fetchall()
for f in k:
    mycursor.execute("SELECT slno FROM review ORDER BY RAND() limit 20")
    j = mycursor.fetchall()
    tot=[]
    for i in j:
        tot.append(i[0])
    mycursor.execute("UPDATE `movies` SET `comment` = '"+str(tot)+"' WHERE `slno` = '"+str(f[0])+"'")
    link.commit()
'''
'''#keyword
keyword =  pd.read_csv('tmdb.csv')
j=list(keyword['keywords'])

mars=''
for i in j:
    data = json.loads(i)
    for element in data:
        for x,y in element.items():
            if(isinstance(y,int)):
                mars=y
                #print(y)
            else:
                mycursor.execute("SELECT * FROM keywords WHERE id='"+str(mars)+"'")
                j = mycursor.fetchall()
                if(mycursor.rowcount==0):
                    exclude = set(string.punctuation)
                    y = ''.join(ch for ch in y if ch not in exclude)
                    mycursor.execute("INSERT INTO `keywords` (`id`, `keyword`) VALUES ('"+str(mars)+"','"+y+"')")
                    link.commit()
                    #print(y)
'''
'''#idea to idea
f = open("content.txt", "w")
keyword =  pd.read_csv('tmdb.csv')
j=list(keyword['keywords'])

mars=[]
mar=''

for i in j:
    data = json.loads(i)
    for element in data:
        for x,y in element.items():
            if(isinstance(y,int)):
                mar = y
                #print(y)
            else:
                if(mar not in mars):
                    mars.append(mar)
                    exclude = set(string.punctuation)
                    y = ''.join(ch for ch in y if ch not in exclude)
                    f.write(str(mar)+" "+y+"\n")
#print(mars)
f.close()

'''
'''#genre
genre=  pd.read_csv('tmdb.csv')
j=list(genre['genres'])

mars=''
for i in j:
    data = json.loads(i)
    for element in data:
        for x,y in element.items():
            if(isinstance(y,int)):
                mars=y
                #print(y)
            else:
                mycursor.execute("SELECT * FROM genre WHERE id='"+str(mars)+"'")
                j = mycursor.fetchall()
                if(mycursor.rowcount==0):
                    mycursor.execute("INSERT INTO `genre` (`id`, `name`) VALUES ('"+str(mars)+"','"+y+"')")
                    link.commit()
                    #print(y)
'''

'''#year

mycursor.execute("SELECT release_date FROM movies")
j = mycursor.fetchall()
m=1
#j.append(('19-05-99',))
for i in j:
    k = i[0].split('-')
    print(k)
    if(int(k[2])<20):
        print('20'+k[2])
        mycursor.execute("UPDATE `movies` SET `year` = '"+('20'+k[2])+"' WHERE `slno` = '"+str(m)+"'")
        link.commit()
        m+=1
    else:
        print('19'+k[2])
        mycursor.execute("UPDATE `movies` SET `year` = '"+('19'+k[2])+"' WHERE `slno` = '"+str(m)+"'")
        link.commit()
        m+=1
'''

''' #photo image
imgurl=  pd.read_csv(r'dataimg.txt', sep=" ", header=None)
j=list(imgurl[[0,4]][4])
k=1
for i in j:
    mycursor.execute("UPDATE `movies` SET `image` = '"+str(i)+"' WHERE `slno` = '"+str(k)+"'")
    link.commit()
    k+=1
    #print(j[i])

'''
