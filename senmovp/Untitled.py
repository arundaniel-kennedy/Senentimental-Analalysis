import joblib
import re
from nltk.corpus import stopwords
import string

forest = joblib.load('forest.pkl')
vectorizer = joblib.load('bow.pkl')

comment ="entertainment more disposable than hanna-barberas half-hour cartoons ever weres"

def reviewWords(review):
    data_train_num = re.sub(r'[0-9]+', 'number', review)  # Converting numbers to "NUMBER"
    data_train_lower = review.lower()              # Converting to lower case.
    data_train_split = data_train_lower.split()            # Splitting into individual words.
    stopWords = set(stopwords.words("english") )
    meaningful_words = [w for w in data_train_split if not w in stopWords]     # Removing stop words.
    return( " ".join( meaningful_words ))

cleanWords=[]
cleanWords.append(reviewWords(comment))
data_test_features = vectorizer.transform(cleanWords)
result = forest.predict(data_test_features)

print(result[0])
