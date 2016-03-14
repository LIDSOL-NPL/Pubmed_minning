import sys
import glob
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint


parser = argparse.ArgumentParser(description='cos classify some files')
parser.add_argument('archivos', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

Corpus=[]
for archivo in args.archivos:
    Corpus.append(archivo.read())    


documents=Corpus
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix     = tfidf_vectorizer.fit_transform(documents)

print tfidf_matrix.shape


cosine_similarity(tfidf_matrix[:], tfidf_matrix)
print cosine_similarity(tfidf_matrix[:], tfidf_matrix)


names=[]    
for i in range(len(Corpus_titles)):
    names.append(Corpus_titles[i][len(path)+1:])

print names
