#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PCL2-Ue4-Aufgabe 2
# Monika Ciemiega 15-919-368

from lxml import etree	
import random
import bz2
from urllib.request import urlopen


def gettitles(infile, testfile, trainfile, k):
    """Creates testfile with k randomly chosen Wikipedia titles
       and trainfile with all the remaining ones."""
	
    titles = etree.iterparse(infile, tag="{http://www.mediawiki.org/xml/export-0.10/}title")
    print ("I made titles")
	
    #Reservoir sampling algorithm to find k random titles (cf. lecture slides)
    reservoir = []
    for t, (action, item) in enumerate(titles):
        if t < k:
            reservoir.append(item.text)
        else:
            m = random.randint(0,t)
            # Replaces the title in position m with new random title
            # and writes the discarded title into trainfile 
            if m < k:
                try:
                    trainfile.write(reservoir[m] + "\n")
                except:
                    trainfile.write("Title Error" + "\n")
                reservoir[m] = item.text
							
    #Write the k random titles in reservoir into the testfile.
    for title in reservoir:
        testfile.write(title + "\n")
	
	
	
def main ():
    file = urlopen("https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2")
    f = bz2.open(file)
    
    test = open("testfile.txt", 'w')
    train = open("trainfile.txt", 'w')
    n = 30
	
    gettitles(f, test, train, n)
    
	#Closing of the opened documents:
    test.close()
    train.close()
    f.close()
 
if __name__ == "__main__":
    main()
