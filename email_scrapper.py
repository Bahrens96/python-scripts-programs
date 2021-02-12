#! python3
import re
import pyperclip

# Create a regex for email addresses
emailRegex = re.compile(r'''
                        #some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+-]+         # name part
@                        # @ symbol
[a-zA-Z0-9_.+-]+         #domain name part
,?
          
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedEmail = emailRegex.findall(text)

# This list stores email address with a semi colon
emailsWithSemiColon = []

#This for loop adds a semi colon to each email address
for emailAddress in extractedEmail:
	originalEmail = emailAddress
	semicolon = ';'
	newEmail = ''.join((originalEmail,semicolon))
	emailsWithSemiColon.append(newEmail)
   
# Copy the extracted email/phone to the clipboard
results = '\n'.join(emailsWithSemiColon)
pyperclip.copy(results)
