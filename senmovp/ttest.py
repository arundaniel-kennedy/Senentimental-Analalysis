import pandas as pd
import mysql.connector
import json
import string

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'movie',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
mycursor = link.cursor()

tup = (257, '262504', 'Allegiant', 'Beatrice Prior and Tobias Eaton venture into the world outside of the fence and are taken into protective custody by a mysterious agency known as the Bureau of Genetic Welfare.', '09-03-16', '2016', '121', 'en', '5.9', 'Released', '//upload.wikimedia.org/wikipedia/en/thumb/f/f8/Allegiantfilmposter.jpg/220px-Allegiantfilmposter.jpg', '[3047, 1665, 4146, 2383, 104, 70, 1312, 3323, 4122, 3509, 2954, 1844, 2789, 577, 2200, 2074, 1239, 796, 2526, 1987, 4544]', '[12, 878]', '[818, 2020, 4565, 9663, 162988, 206298, 223438]', 'Adventure')
#print(tup)
tup = list(tup)
tup.append(98)
print(tuple(tup))

'''
fdata = pd.read_csv(r'genlang.txt', sep=" ", header=None)
imgurl=  pd.read_csv(r'dataimgn.txt', sep=" ", header=None)
data=pd.read_csv('tmdb.csv')
sim=pd.read_csv("t2.csv")

y = ["Pandora's Box"]
l=[]
for i in y:
    #exclude = set(string.punctuation)
    #exclude = exclude-{':','&','_','(',')','-'}
    #i = ''.join(ch for ch in i if ch not in exclude)
    #print(exclude)
    mycursor.execute('SELECT * FROM movies where title="'+i+'"')
    myresult = mycursor.fetchone()
    l.append(myresult)
print(l)

def srt(s):
  return s[1]

id = 426469

mycursor.execute("SELECT title FROM movies where id='"+str(id)+"'")
name = mycursor.fetchone()
name = name[0]


s=sim[name].sum()
d=[]
for i in sim.columns[1:]:
  sm=(sim[name]*sim[i]).sum()/s
  d.append([i.replace(' ',' '),sm])
d=sorted(d,key=srt,reverse=True)
d= [item for sublist in d for item in sublist]
#k=d.find(0)
#for i in d[:19:2]:
print(d[2])


mycursor.execute("SELECT * FROM movies where title='"+d[::2][1]+"'")
p = mycursor.fetchall()
print(p)


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
