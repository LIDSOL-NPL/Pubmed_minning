#import argparse
#from pprint import pprint

#parser = argparse.ArgumentParser(description='cos classify some files')
#parser.add_argument('--archivos', type=argparse.FileType('r'), required=False, nargs='*')
#args = parser.parse_args()

# args tiene una lista de archivos abiertos! checa:
#pprint(args.archivos)

# puedes hacer algo como:
#for archivo in args.archivos:
#    pprint(archivo.read()[0:70])


import glob
path="/home/neo/Documents/Trabajo/Trabajo_academico/CursoCCGBioinfo/Carlos_Natural_Lenguage_Procesing/LearningSciKit/"
Corpus_titles = glob.glob( path + "*.txt")
print Corpus_titles 

Corpus=[]

for title in Corpus_titles:
    with open(title,'r') as myfile:
        data=myfile.read().remplace('\n',' ')
        print data;
        
    Corpus.append(data)
