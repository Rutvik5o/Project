#user input

#using slicing function


email = input("Please enter your email address=> \n").strip()

print(email)  

#email = "user@example.com"

username_part= email[:email.index("@")]

# username_part will be 'user'

#email[:email.index("@")] means "take the substring of email from the start up to (but not including) the index of the "@" character".

#email.index("@") finds the position (index) of the "@" character in the email string.


domain_name = email[email.index("@")+1:]



output= (f"Your username is '{username_part}' & your domain is '{domain_name}'")

print(output)


'''
Explanation

we are using the strip function to remove any whitespace. The code will search for te index of the "@" sign i the user input. The index is used to divide the mail into username & domain parts.
'''