import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from sklearn.svm import SVC
# nltk.download()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
# file_path = 'C:\\Users\\grand\\text mining'
file_path = 'C:\\Users\\ouchu\\text mining\\data'
stop_words = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
text = []
for num in range(1, 1096):
    with open((file_path+'\\PA1-data\\'+ str(num) + ".txt"), mode='r') as f:
        line = f.read()
        # if num == 11:
        #     print(line)
        line = line.lower()
        word_list = nltk.word_tokenize(line)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        text.append(lemmatized_output)
        # text.append(line)

lab = []
with open((file_path+'\\training'+ ".txt"), 'r') as f:
    lab = f.read()
lab = lab.split('\n')
x_train = []
x_test = []
y_train = []
y_test = []
label = -1
for i in lab:
    i = i.split()
    i = list(map(int, i))
    
    for j in range(1, len(i)):
        
        if j <= 13:
            # print(i[j], text[i[j]], i[0])
            x_train.append(text[i[j] - 1])
            y_train.append(i[0])
            continue
        # print(i[j])
        x_test.append(text[i[j] - 1])
        y_test.append(i[0])
texts = x_test + x_train

TFlDF = TfidfVectorizer( lowercase=True, stop_words=set(stop_words), min_df=1)
TFIDF_vectors = TFlDF.fit_transform(texts)
length = len(x_test)


x_test = TFIDF_vectors[:length]
x_train = TFIDF_vectors[length:]
#SVM_model = SVC(kernel='linear', C=1.0)
SVM_model = SVC(kernel='rbf', gamma='scale', C=1.0)
# SVM_model = SVC(kernel='poly', degree=2, coef0=1, C=1.0)
SVM_model.fit(x_train,y_train)
predicted_results = []
expected_results = []
expected_results.extend(y_test)
predicted_results.extend(SVM_model.predict(x_test))
print(predicted_results)

print(metrics.classification_report(expected_results, predicted_results))