import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords, movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

def build_naive_bayes_model():

    df = pd.read_csv("questions_processed_adapted.txt", sep=';;', names=['questions', 'tags'], engine='python')
    # print(df.head())

    stopset = set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)
    # print(stopset)
    # print(vectorizer)

    y=df.tags
    x=vectorizer.fit_transform(df.questions)
    # print(y)
    # print(x)
    # print(x.shape, y.shape)

    # On peut ajouter ceci si on veut diviser notre dataset entre 2 parties:
    # une partie pour le training et une autre pour le test
    # x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

    clf = naive_bayes.MultinomialNB()
    clf.fit(x, y)

    from sklearn.model_selection import cross_val_predict
    predicted = cross_val_predict(clf, x, y, cv=10)
    print (metrics.accuracy_score(y, predicted)) 
    
    #predicted = clf.predict(x)
    #k=np.mean(predicted == y)
    #print(str(k))

    # dans le cas ou on a un training set, on peut mesurer la pr"cision de notre modèle
    # accuracy=roc_auc_score(y_test, clf.predict_proba(x_test)[:,1])
    # print(accuracy)


#     return the classifier model that we build with bayes

    return clf,vectorizer
