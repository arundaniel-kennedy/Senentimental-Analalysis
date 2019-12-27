from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string

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

print(totneg,totpos)
if(totneg>totpos):
    print("0")
elif(totneg<totpos):
    print("1")
else:
    print("0")
