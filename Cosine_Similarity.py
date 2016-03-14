import sys
import glob
import argparse
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint


parser = argparse.ArgumentParser(description='cos classify some files')
parser.add_argument('archivos', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

titulos=[]
Corpus=[]
for archivo in args.archivos:
    titulos.append(os.path.basename(archivo.name))
    Corpus.append(archivo.read())    


documents=Corpus
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix     = tfidf_vectorizer.fit_transform(documents)


i = 0
#cosine_similarity(tfidf_matrix[:], tfidf_matrix)
for row in cosine_similarity(tfidf_matrix[:], tfidf_matrix):
    r = [ titulos[i].strip("\n"),]
    i += 1
    print ",".join(r + [str(v) for v in row])
        



# names=[]    
# for i in range(len(Corpus_titles)):
#     names.append(Corpus_titles[i][len(path)+1:])

# print names
