#!/usr/bin/env python3
import csv

f = open("download/france2014.txt", encoding="latin1")
cog = csv.DictReader(f, delimiter='\t')

def traite_insee(ch) :
    ch = ch.replace('\x8c', '\u0152') # OE
    ch = ch.replace('\x9c', '\u0153') # oe
    return ch

tncc2art = {
  '0':'',
  '1':'',
  '2':'Le ',
  '3':'La ',
  '4':'Les ',
  '5':"L'",
  '6':'Aux ',
  '7':'Las ',
  '8':'Los ',
}

tncc2ch = {
  '0':'de',
  '1':"d'",
  '2':'du',
  '3':'de la',
  '4':'des',
  '5':"de l'",
  '6':'des',
  '7':'de las',
  '8':'de los',
}

print('dc', 'actual', 'r', 'd', 'ct', 'cheflieu', 'pole', 'tncc', 'nom', 'nomsa', sep='\t' )
for l in cog :
    if l['ACTUAL'] not in ('4', '6') :
        print(l['DEP']+l['COM'], l['ACTUAL'], l['REG'], l['DEP'], l['CT'], l['CHEFLIEU'], l['POLE'],
                l['TNCC'], tncc2art[l['TNCC']] + traite_insee(l['NCCENR']), traite_insee(l['NCCENR']), sep='\t')
