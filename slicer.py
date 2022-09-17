#get user email adress

email = input("What is your email adress?: ").strip()

#slice out user name

user = email[:email.index("@")]

#slice domanin name

domain = email[email.index("@")+1:]

#format message

output = "Your user name is {} and your domain name is {}".format(user,domain)

#display output message

print(output)
