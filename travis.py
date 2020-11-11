known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! I'm Travis.")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello, {} !".format(name))
        remove = input("Do you want to be removed from the system? (y/n)").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print("You were removed.")
        elif remove == "n":
            print("No problem. I didn't want you to leave anyway.")
            
            
    else:
        print("Hmmm I don't think we have met yet.")
        add_me = input("Would you like to be added to the system? (y/n)").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("You were successfully added.")
        elif add_me == "n":
            print("No worries. See you around.")
            
