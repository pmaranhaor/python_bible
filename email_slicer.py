# get user email address
email = input("What is your email address? ").strip()

# slice out user name
username = email[:email.index("@")]

# slice domain name

domain = email[email.index("@")+1:]

# format message

message = "Your username is {} and your domain is {}".format(username, domain)

# display output message
print(message)


