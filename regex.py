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

'''

import re

def email_address_check(email):

	if not re.match(r'([a-zA-Z])+@([a-zA-Z0-9])+\.[a-zA-Z.]{2,5}', email):
		print email + " does not match"
	else:
		print email + " matches"

email_address_check('simon@logicdesign.co.uk')
email_address_check('simon@logicdesign.com')
