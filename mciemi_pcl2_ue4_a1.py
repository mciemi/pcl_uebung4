#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PCL2-Ue4-Aufgabe 1
# Monika Ciemiega 15-919-368

import glob
import re
from lxml import etree

def getfreqwords(indir, outfile):
    """Creates file with the 20 most frequent sentences of the corpus"""
   #indir: Verzeichnis mit xml dateien
   #outfile: textdatei für ausgabe

    name = str(indr) + '\SAC_Jahrbuch*mul.xml'
    filenames = glob.glob(name)
    writefile = open("temporary_memory.txt", 'w')
	
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
			    					
# Schritt 2: lemmasatz-hash zuweisen								
                        s_hash = hash(sentence)
						
# Schritt 3: hash zu dict, prüfen ob schon mal drin
		    			#Check if sentence has been used before and add to/increase dict.
                        if s_hash not in sentence_hashes:
                            sentence_hashes[s_hash] = 1
							
# Schritt 4: Satz zwischenspeichern						
                            # Write the sentence with its hash into the temporary memory
                            # in order to not use up memory with a list.							
                            writefile.write(s_hash + ": " + sentence + '\n')
                        else:
                            sentence_hashes[s_hash] += 1
						#Delete the s_hash variable for each sentence to free memory.
                        del s_hash

    print("I have gone through all sentences")						
	
    #Create a new list with the 20 most frequent hashes.
    top_hashes = sorted(sentence_hashes, key=sentence_hashes.get, reverse=True)[0:20]
    #Delete the dictionary of all hashes to free memory space.
    del sentence_hashes
	
    print("I own a list of the 20 most frequent hashes")
	
# Schritt 5: häufigste 20 finden und ausschreiben
    #Search for the sentences to the top 20 hashes, write them into outfile.
    for h in top_hashes:
        pattern = str(h) + ":\s" + "(.*)" + "\n"
        match = re.search(pattern, writefile)
        outfile.write(match.group(1) + "\n")
    
    writefile.close()
	
   
   
def main():
    i = "C:\Users\User\Documents\UZH\PCL\PCL ubungen\ubung 4\SAC"
    o = open("top_20_sentences.txt", 'w')
    getfreqwords(i, o)

    o.close()
 
#if __name__ == "__main__":
 #   main()