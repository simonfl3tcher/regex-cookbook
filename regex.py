#!/usr/bin/env python

'''

Regex cookbook

. - Matches any character, except for line breaks if dotall is false.
* - Matches 0 or more of the preceding character.
+ - Matches 1 or more of the preceding character.
? - Preceding character is optional. Matches 0 or 1 occurrence.
\d - Matches any single digit
\w - Matches any word character (alphanumeric & underscore).
[XYZ] - Matches any single character from the character class.
[XYZ]+ - Matches one or more of any of the characters in the set.
$ - Matches the end of the string.
^ - Matches the beginning of a string.
[^a-z] - When inside of a character class, the ^ means NOT; in this case, match anything that is NOT a lowercase letter. 
(|) - one string or the other, either side of the pipe
i - matches upper or lowercase it doesn't matter

^ : start of string
[ : beginning of character group
a-z : any lowercase letter
A-Z : any uppercase letter
0-9 : any digit
_ : underscore
] : end of character group
* : zero or more of the given characters
$ : end of string

All regexes below are my own thought out regular expressions, if you feel the need to use them then please by all means.

'''

import re

# Checks if email address is valid

def email_address_check(email):

	if not re.match(r'([a-zA-Z])+@([a-zA-Z0-9])+\.[a-zA-Z.]{2,5}', email):

		print email + " does not match"

	else:

		print email + " matches"

email_address_check('simon@logicdesign.co.uk')
email_address_check('simon@logicdesign.com')

# Check if string starts with with AB or AC preceeded with 8-10 numbers for example AC12345678

def check_string_ac(string):

	if not re.match(r'^(AB|AC)\d{8,12}$', string):

		print string + " does not match"

	else: 

		print string + " matches"


check_string_ac('AC12345678')
check_string_ac('AC123456789999999')

# does string contain image extentions
	
def check_if_is_image(string):

	# it does a match as to wether the upper and lowercase extentions have been used.

	if not re.match(r'([a-zA-Z0-9])+(\.(?i)(gif|jpg|jpeg|tiff|png))+$', string):

		print string + " does not match"

	else:

		print string + " matches"

check_if_is_image('image.jpg')
check_if_is_image('image.JPG')
check_if_is_image('file.php')


# does string contain 2 letters either LD or AZ at the start, followed by 5 numbers and a (.) then a domain name. For example LD89780.simonfletcher.co.uk


def do_check(string):

	if not re.match(r'^((LD|AZ)\d{5})(\.)([a-zA-Z0-9]+\.[a-zA-Z.]{2,5})$', string):

		print string + " does not match"

	else:

		print string + " matches"


do_check('LD89780.simonfletcher.co.uk');
do_check('LD89780.simonfletcher');


def replace_span(string):

	output = re.sub(r'^(<(span)>)(.*)(</(span)>)$', r'<strong>\3</strong>', string)

	print output


replace_span('<span>Replace span with strong</span>')

