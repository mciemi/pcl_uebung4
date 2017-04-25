# pcl_uebung4

Monika Ciemiega 

A1: Ich habe zu Beginn die Hashes der lemmatisierten Sätze im Dictionary als keys gespeichert, mit ihren Häufigkeiten als values. Da ich jedoch nicht von den Hashes direkt auf Sätze schliessen kann, hatte ich diese in einem externen outfile gespeichert, mit deren Hash am Zeilenanfang, sodass ich danach, mit der sortierten und gekürzten Liste der 20 häufigsten, die Sätze darin suchen konnte. Natürlich war das ein Speicher- und Zeitproblem, da ich mit Regex 20 mal das ganze file mit den Sätzen durchsuchen musste. Somit schien es mir unterm Strich dennoch effizienter, im dictionary statt dem Hash den lemmatisierten Satz als key zu nehmen, obwohl dieser viel mehr Speicher verbraucht.

A2: Das ganze clear-statement habe ich ebenfalls von der stackoverflow-Lösung unter http://stackoverflow.com/questions/12160418/why-is-lxml-etree-iterparse-eating-up-all-my-memory adaptiert.

Reflexion:
a) Ich habe zum ersten mal mit git und github gearbeitet, und mit dem Reservoir Sampling sowie auch mit hashes (obwohl ich diese Methode wieder verwerfen musste, aber damit gearbeitet hatte ich trotzdem). 
b) 15h
