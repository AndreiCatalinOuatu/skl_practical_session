"""
Acest script citeste date dintr-un fisier si incearca sa calculeze care este cuvantul ce contine cele mai
multe caractere.
"""

import io
	
# Citim datele
f = open("input.txt", "r")
no_of_chars = 0
word = ""
for line in f.readlines():
	'''
	Citim linie cu linie
	'''
	if no_of_chars < len(line.strip("\n")):
		no_of_chars = len(line.strip("\n"))
		word = line

print("Cuvantul care contine cele mai multe caractere este %s" % word)
print("Lungimea acestuia este %d" % no_of_chars)