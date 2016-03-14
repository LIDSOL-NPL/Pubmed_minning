import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='cos classify some files')
parser.add_argument('--archivos', type=argparse.FileType('r'), required=False, nargs='*')
args = parser.parse_args()

# args tiene una lista de archivos abiertos! checa:
pprint(args.archivos)

# puedes hacer algo como:
for archivo in args.archivos:
    pprint(archivo.read()[0:70])





documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print tfidf_matrix.shape

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
array([[ 1.        ,  0.36651513,  0.52305744,  0.13448867]])
