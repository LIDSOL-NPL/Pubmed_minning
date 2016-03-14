import sys
import glob
import argparse
import os
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint


parser = argparse.ArgumentParser(description='Cosine classify some files')
parser.add_argument('archivos', type=argparse.FileType('r'), nargs='+', help='one or more files, or a glob like path_to/*txt')
args = parser.parse_args()

titulos=[]
Corpus=[]
for archivo in args.archivos:
    titulos.append(os.path.basename(archivo.name))
    Corpus.append(archivo.read())    


documents=Corpus
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix     = tfidf_vectorizer.fit_transform(documents)


dicts = {t:{} for t in titulos}
i = 0
for row in cosine_similarity(tfidf_matrix[:], tfidf_matrix):
    tmp = {}
    j = 0
    for t in list(row):
        tmp[ titulos[j]]=t 
        j += 1
    x = tmp
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
    dicts[titulos[i]] = sorted_x

    i += 1

pprint(dicts)        



# names=[]    
# for i in range(len(Corpus_titles)):
#     names.append(Corpus_titles[i][len(path)+1:])

# print names
