import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download()
from sklearn. naive_bayes import BernoulliNB
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer

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

# print(texts[0:10])
from sklearn.feature_extraction.text import CountVectorizer
length = len(x_test)
binary_vectorizer = CountVectorizer(binary=True)
binary_vectors = binary_vectorizer.fit_transform(x_test + x_train)

x_test = binary_vectors[:length]
x_train = binary_vectors[length:]

model = BernoulliNB()
model.fit(x_train,y_train)
predicted_results = []
expected_results = []
expected_results.extend(y_test)
predicted_results.extend(model.predict(x_test))
from sklearn import metrics
print(metrics.classification_report(expected_results, predicted_results))
