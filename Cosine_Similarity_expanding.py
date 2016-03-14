
import sys
import glob
#directory=sys.argv[1]
#path= directory
#path="/home/neo/Documents/Trabajo/Trabajo_academico/CursoCCGBioinfo/Carlos_Natural_Lenguage_Procesing/LearningSciKit/"
path="/home/neo/Documents/Trabajo/Trabajo_academico/CursoCCGBioinfo/Carlos_Natural_Lenguage_Procesing/Data_of_them/corpusTareaSimilitud"
#path=""

Corpus_titles = glob.glob( path + "/*.txt")
print Corpus_titles 

Corpus=[]

for title in Corpus_titles:
    with open(title,'r') as myfile:
        data=myfile.read().replace('\n',' ')
        print data;
        Corpus.append(data)

#documents = (
#"The sky is blue",
#"The sun is bright",
#"The sun in the sky is bright",
#"We can see the shining sun, the bright sun"
#)
documents=Corpus
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print tfidf_matrix.shape

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity(tfidf_matrix[:], tfidf_matrix)

print cosine_similarity(tfidf_matrix[:], tfidf_matrix)
#print Corpus_titles

names=[]    
for i in range(len(Corpus_titles)):
    names.append(Corpus_titles[i][len(path)+1:])


print names


