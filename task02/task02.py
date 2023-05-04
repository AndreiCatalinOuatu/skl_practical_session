"""
Acest script citeste date dintr-un fisier si incearca sa calculeze care este cuvantul ce contine cele mai
multe caractere.
"""

import io
	
	# Citim datele
f = open("input.txt","w")
no_of_chars = 0
word = ""
for line in f.readline():
'''
Citim linie cu linie
'''
	if no_of_chars > len(line):
	no_of_chars = len(line)
		word = line

print("Cuvantul care contine cele mai multe caractere este %s" % word)
print("Lungimea acestuia este %d" % no_of_chars)