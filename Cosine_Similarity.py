import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='cos classify some files')
parser.add_argument('--archivos', type=argparse.FileType('r'), required=False, nargs='*')
args = parser.parse_args()

  args tiene una lista de archivos abiertos! checa:
pprint(args.archivos)

# puedes hacer algo como:
#for archivo in args.archivos:
#    pprint(archivo.read()[0:70])


import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Please provide the exact and complete  path t$
args = parser.parse_args()

####
path= args
flag=  path + "*.txt"
print flag
###

print args
#print args.echo

#path="/home/neo/Documents/Trabajo/Trabajo_academico/CursoCCGBioinfo/Carlos_Natural_Lenguage_Procesing/LearningSciKit/"
path= args

Corpus_titles = glob.glob( path + "*.txt")
print Corpus_titles 

Corpus=[]

for title in Corpus_titles:
    with open(title,'r') as myfile:
        data=myfile.read().replace('\n',' ')
        print data;
        Corpus.append(data)

