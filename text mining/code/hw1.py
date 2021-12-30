

import nltk
import numpy as np
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
# nltk.download()
from sklearn.feature_extraction.text import TfidfVectorizer
# file_path = 'C:\\Users\\grand\\text mining'
file_path = 'C:\\Users\\ouchu\\text mining'
stop_words = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
text = []
for num in range(1, 1096):
    with open((file_path+'\\PA1-data\\'+ str(num) + ".txt"), mode='r') as f:
        line = f.read()
        line = line.lower()
        word_list = nltk.word_tokenize(line)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        text.append(lemmatized_output)

TFlDF = TfidfVectorizer( lowercase=True, stop_words=set(stop_words))
TFIDF_vectors = TFlDF.fit_transform(text)
# print(TFIDF_vectors.toarray())

# print(TFIDF_vectors[0].indices)

for num in range(1, 4):
    if num == 2:
        continue
    if num > 3:
        break
        
    i = num - 1
    term = np.empty([0, 2])
    for j in range(TFIDF_vectors.indptr[i], TFIDF_vectors.indptr[i + 1]):
        row= np.array([int(TFIDF_vectors.indices[j]), str(TFIDF_vectors.data[j])])
        term = np.append(term,[row],axis= 0)
  
    
    term = sorted(term , key=lambda a_entry: int(a_entry[0])) 
    with open((file_path+'\\result\\'+ str(num) + ".txt"), mode='w+', newline='\n') as f:
        f.writelines(str(TFIDF_vectors.indptr[i + 1] - TFIDF_vectors.indptr[i]))
        f.writelines('\n')
        f.writelines('t_index,tf-idf')
        f.writelines('\n')
        for i in term:
            f.writelines(i[0] + ',' + i[1]+  '\n')
print(cosine_similarity(TFIDF_vectors, TFIDF_vectors)[0, 1])