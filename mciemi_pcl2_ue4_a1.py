#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PCL2-Ue4-Aufgabe 1
# Monika Ciemiega 15-919-368

import glob
from lxml import etree

def getfreqwords(indir, outfile):
    """Creates file with the 20 most frequent sentences of the corpus"""

    name = str(indir) + '\SAC_Jahrbuch*mul.xml'
	
    all_sentences = dict()
    # The "[:2]" is the exit condition, if deleted it will go through all files.
    for file in glob.glob(name)[:2]:
        doc = etree.parse(file)
        root = doc.getroot()
        for child in root:
            for d in child:
    		#Going only through all "div" tags which include the sentences.
                if d.tag == "div":
                    for sent in d:	
                        #Only if sentence has 6+ tokens, create lemmatised sentence.
                        if len(sent)>5: 
                            sentence = ''
                            for w in sent:
				# Create lemmatised sentence to get its hash value.
                                try:
                                    sentence += w.get("lemma")
                                    sentence += " "
				#Exception for when it's not a "w" tag and the w.get is None.
                                except TypeError:
                                    pass			
		    	#Check if sentence has been used before and add to/increase dict.
                        if sentence not in all_sentences:
                            all_sentences[sentence] = 1					
                        else:
                            all_sentences[sentence] += 1
                        #Delete the sentence variable for each sentence to free memory.
                        del sentence					
    #Create a new list with the 20 most frequent hashes.
    top_hashes = sorted(all_sentences, key=all_sentences.get, reverse=True)[0:20]
    #Delete the dictionary of all hashes to free memory space.
    del sentence_hashes
	
    #Search for the sentences to the top 20 hashes, write them into outfile.
    for s in top_hashes:
        outfile.write(s + "\n")
	 
   
def main():
    i = r"C:\Users\User\Documents\UZH\PCL\PCL ubungen\ubung 4\SAC"
    o = open("top_20_sentences.txt", 'w')
    getfreqwords(i, o)

    o.close()
 
if __name__ == "__main__":
    main()
