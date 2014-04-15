#!/usr/bin/env python

import re

'''

Regex cookbook

^		- start of string
[		- beginning of character group
a-z		- any lowercase letter
A-Z		- any uppercase letter
0-9		- any digit
_		- underscore
]		- end of character group
$		- end of string
. 		- Matches any character, except for line breaks if dotall is false.
* 		- Matches 0 or more of the preceding character.
+ 		- Matches 1 or more of the preceding character.
? 		- preceed character is optional. Matches 0 or 1 occurrence.
\d 		- Matches any single digit
\w 		- Matches any word character (alphanumeric & underscore).
[XYZ] 	- Matches any single character from the character class.
[XYZ]+ 	- Matches one or more of any of the characters in the set.
(|)		- one string or the other, either side of the pipe
i 		- matches upper or lowercase it doesn't matter

All regexes below are my own thought out regular expressions, if you feel the need to use them then please by all means.


'''

variable = [
	'([a-zA-Z])+@([a-zA-Z0-9])+\.[a-zA-Z.]{2,5}', # email address check
	'^(https?:\/\/)?(www.)?([\da-z\.-]+)\.([a-z\.]{2,6})\/?$', # check url
	'^(AB|AC)\d{8,12}$', # Check if string starts with with AB or AC preceeded with 8-10 numbers for example AC12345678
	'([a-zA-Z0-9])+(\.(?i)(gif|jpg|jpeg|tiff|png))+$', # does string contain image extentions
	'^#([a-f0-9]{6}|[a-f0-9]{3})', # matches a colour hex value i.e. #a5a5a5 or #fff
	'^((LD|AZ)\d{5})(\.)([a-zA-Z0-9]+\.[a-zA-Z.]{2,5})$', # Special
	'^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$', # Matching an HTML Tag 
	'(.*[?=.*A-Z])([?=.*a-z])(?=.*\d).{6,15}$', # Username check
	'(([A-Z]{2})\s?(\d{2})\s?([A-Z]){3})', # match english car registration
	'(.*[?=.*A-Z])([?=.*a-z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{6,15}$', # Special
	'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}?:\d{2,4})$', # IP Address Check
	'^is_unique\[(.*)\]' # Get value between is_unique[]
]


# # Checks if email address is valid

def do_check(regex, email):

	if not re.match(r'' + regex, email):

		print email + " does not match"

	else:

		print email + " matches"


def replace_span_with_strong(string):

	output = re.sub(r'^(<(span)>)(.*)(</(span)>)$', r'<strong>\3</strong>', string)

	print output


replace_span_with_strong('<span>Replace span with strong</span>')

# # Email address check

do_check(variable[0], 'simon@logicdesign.co.uk')
do_check(variable[0], 'simon@logicdesign.com')

# # URL check

do_check(variable[1], 'https://www.google.co.uk/')
do_check(variable[1], 'google.co.uk///')


# # Check if string starts with with AB or AC preceeded with 8-10 numbers for example AC12345678

do_check(variable[2], 'AC12345678')
do_check(variable[2], 'AC123456789999999')


# # does string contain image extentions

do_check(variable[3], 'image.jpg')
do_check(variable[3], 'image.JPG')
do_check(variable[3], 'file.php')
	

# # matches a colour hex value i.e. #a5a5a5 or #fff

do_check(variable[4], '#a5a5a5')
do_check(variable[4], '#fff')
do_check(variable[4], 'a7a7a7')


# # does string contain 2 letters either LD or AZ at the start, followed by 5 numbers and a (.) then a domain name. For example LD89780.simonfletcher.co.uk

do_check(variable[5], 'LD89780.simonfletcher.co.uk')
do_check(variable[5], 'LD89780.simonfletcher')


# # Username must contain one uppercase and one lowercase charater and two digits

do_check(variable[7], 'Fletcher890')
do_check(variable[7], 'Fletc0her')


# # Match an generic english car registration 

do_check(variable[8], 'AD 64 HGV')
do_check(variable[8], 'AD64HGV')
do_check(variable[8], '64ADHGV')


# # Check password for one capital letter and one special character. The string can only be 6-15 characters long

do_check(variable[9], 'fLetch/er89')
do_check(variable[9], 'fLetcher89')


# # Matching an IP Address including optional port number

do_check(variable[10], '73.126.33.108:3000')
do_check(variable[10], '73.126.33')

# # match the value within the "is_unique[]" 
do_check(variable[11], 'is_unique[user.email]')
do_check(variable[11], 'is_unique[user.email')
