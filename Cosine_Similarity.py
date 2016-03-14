import sys
import glob
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint


parser = argparse.ArgumentParser(description='cos classify some files')
parser.add_argument('archivos', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

titulos=[]
Corpus=[]
for archivo in args.archivos:
    titulos.append(archivo.name)
    Corpus.append(archivo.read())    


documents=Corpus
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix     = tfidf_vectorizer.fit_transform(documents)


i = 0
cosine_similarity(tfidf_matrix[:], tfidf_matrix)
for row in cosine_similarity(tfidf_matrix[:], tfidf_matrix):
    print titulos[i]
    i += 1
    pprint(row)

pprint(titulos)

# names=[]    
# for i in range(len(Corpus_titles)):
#     names.append(Corpus_titles[i][len(path)+1:])

# print names
