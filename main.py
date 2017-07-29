""" This script can extract Phone Numbers and Email addresses from the clipboard
	Constraints:
		Area-Code must be of 3 to 5 digits (INDIA)
		Use - or . or (space) to separate Area-Code and Telephone Number
		Telephone Number to be of 8 digits (INDIAN std.)
"""

import sys
import pyperclip
import re

scr = sys.argv

text = str(pyperclip.paste())
#print type(text)

PhoneRegex = re.compile(r"""(
		(\d{3}|\d{4}|\d{5})		# Area-Code
		(-|\.|\s)				# separator
		(\d{,8}) 				# Telephone number
	)""", re.X)

EmailRegex = re.compile(r'''(
		[A-Za-z0-9._]+	# username
		@
		[A-Za-z-.]+		# top-level domain
		\.[A-Za-z]+		# .something
	)''', re.X)

results = []
#print type(PhoneRegex)

#molist = EmailRegex.findall(text)
#print molist

for group in PhoneRegex.findall(text):
	genPhone = '-'.join([group[1], group[3]])
	results.append(genPhone)

for group in EmailRegex.findall(text):
	results.append(group)

if len(results):
	finalstring = '\n'.join(results)
	pyperclip.copy(finalstring)
	print finalstring

else:
	print "No match for any Phone Number or E-mail address found!"

