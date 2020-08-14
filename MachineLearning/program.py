import fetch_data
from cleaning_data import *
from adapt_data import *
from build_model_naive_bayes import *
from svm_classifier import * 

# fetch data
dataFetcher = fetch_data.DataFetcher()
#dataFetcher.fetch()
dataFetcher.extractTags()

# cleaning data
cleaning_data()

# adapt data 'question;;un_seul_tag'
adapt_data_to_naive_bayes()

# build model

clf, vectorizer=build_naive_bayes_model() #naive_bayes
#clf, vectorizer=build_svm_model() #svm


def predict(q):
    qst = np.array([q])
    qst_vector = vectorizer.transform(qst)
    print("Question : " + str(q) + "   ==Prediction==>   " + str(clf.predict(qst_vector)))

# some predicts
qsts=["why is the earth rotating?", "the sun solar system", "the sun solar system", "is there a life in jupiter"]
for q in qsts:
    predict(q)

while True:
    q=input("Entrez votre question :  ")
    predict(q)

# the sun solar system
# which are the brightest stars