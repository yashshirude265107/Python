'''You have a list of email addresses and you want to extract the domain part (the part
 after '@') from each email address.'''
 
emails = [
    "alice@example.com",
    "bob@gmail.com",
    "charlie@yahoo.com",
    "david@company.org"
]

# Create a new list with domains
domains = [email.split('@')[1] for email in emails]

print(domains)
