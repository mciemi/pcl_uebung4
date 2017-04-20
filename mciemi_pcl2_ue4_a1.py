#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PCL2-Ue4-Aufgabe 1
# Monika Ciemiega 15-919-368

import glob
from lxml import etree

def getfreqwords(indir, outfile):
    """Creates file with the 20 most frequent sentences of the corpus"""
   #indir: directory with all the xml files
   #outfile: text file for the most frequent sentences

    name = str(indr) + '\SAC_Jahrbuch*mul.xml'
    filenames = glob.glob(name)
	
    print("I have managed to open it")
	
    sentence_hashes = dict()
    for name in filenames:
        doc = etree.parse(name)
        root = doc.getroot()
        for child in root:
            for d in child:
    		#Going only through all "div" tags which include the sentences.
                if d.tag == "div":
                    for sent in d:
				
# Schritt 1: aus lemmas von satz neuen satz zusammenkleben		
		                #Only if sentence has 6+ tokens, create lemmatised sentence.
                        if len(sent)>5: 
                            sentence = ''
                            for w in sent:
				                #Create lemmatised sentence to get its hash value.
                                try:
                                    sentence += w.get("lemma")
                                    sentence += " "
				                #Exception for when it's not a "w" tag and the w.get is None.
                                except TypeError:
                                    pass
						
# Schritt 3: hash zu dict, prüfen ob schon mal drin
		    			#Check if sentence has been used before and add to/increase dict.
                        if sentence not in sentence_hashes:
                            sentence_hashes[sentence] = 1					
                        else:
                            sentence_hashes[sentence] += 1
						#Delete the s_hash variable for each sentence to free memory.
                        del sentence

    print("I have gone through all sentences")						
	
    #Create a new list with the 20 most frequent hashes.
    top_hashes = sorted(sentence_hashes, key=sentence_hashes.get, reverse=True)[0:20]
    #Delete the dictionary of all hashes to free memory space.
    del sentence_hashes
	
# Schritt 5: häufigste 20 finden und ausschreiben
    #Search for the sentences to the top 20 hashes, write them into outfile.
    for s in top_hashes:
        outfile.write(s + "\n")
	
   
   
def main():
    i = "C:\Users\User\Documents\UZH\PCL\PCL ubungen\ubung 4\SAC"
    o = open("top_20_sentences.txt", 'w')
    getfreqwords(i, o)

    o.close()
 
if __name__ == "__main__":
    main()
