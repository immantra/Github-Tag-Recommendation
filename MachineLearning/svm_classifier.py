from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords, movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn import naive_bayes, svm
from sklearn import  metrics
from sklearn.model_selection import GridSearchCV



def build_svm_model():

    #train the model
    df = pd.read_csv("questions_processed_adapted_train.txt", sep=';;', names=['questions', 'tags'], engine='python')

    stopset = set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)

    y=df.tags
    x=vectorizer.fit_transform(df.questions)

    clf = SGDClassifier()
    clf.fit(x, y)

    from sklearn.model_selection import cross_val_predict
    predicted = cross_val_predict(clf, x, y, cv=10)
    print (metrics.accuracy_score(y, predicted)) 

 #   predicted = clf.predict(x_test)
  #  k=np.mean(predicted == y_test)
  #  print(str(k))
    
    return clf,vectorizer

