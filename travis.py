known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()  #strip - elimina spatiile/capitalize - intotdeauna prima litera este mare

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be remove from the system (y/n)?: ").strip().lower()   #lower - litere mici

        if remove == "y":
            known_users.remove(name) #elimina din lista numele
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
                       
    else:
        print("Hmmm I don't think I have meet you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name) #.append - add to list
        elif add_me == "n":
            print ("No worries, see you around!")

