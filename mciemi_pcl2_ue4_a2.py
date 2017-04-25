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
	
    #Reservoir sampling algorithm to find k random titles (cf. lecture slides)
    reservoir = []
    context = enumerate(titles)
    counter = 0
    for t, (action, item) in context:
        if t < k:
            reservoir.append(item.text)
        else:
            m = random.randint(0,t)
            # Replace the title in position m with new random title
            # and write the discarded title into trainfile 
            if m < k:
                try:
                    trainfile.write(reservoir[m] + "\n")
            # I left this except statement because my terminal had some issues to decode
            # at times (with entering chcp65001 it usually worked), so just in case you'd have 
            # the same problem this will keep the programme from returning an Error
                except:
                    trainfile.write("Title Error" + "\n")
                reservoir[m] = item.text
        # Delete what was already used to free memory space
        item.clear()
        for ancestor in item.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is None:
                del ancestor.getparent()[0]
        # Counter casues the loop to exit after 1000 to check output
        counter += 1
	# If the number is reached, exit loop and write the testfile
        if counter > 1000:
            break
    del context
							
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
