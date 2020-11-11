films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters":[12, 5]
    }

while True:
    choice = input("Which film would you like to watch? ").strip().title()
    if choice in films:

        #check age

        while True:
            age = input("How old are you?").strip()
            if age.isdigit():
                age = int(age)
                if age >= films[choice][0]:

                    #check seats

                    num_seats = films[choice][1]
                    if num_seats > 0:                     
                        print("Enjoy the film!")
                        films[choice][1] = films[choice][1] - 1
                    else:
                        print("Sorry, we are sold out!")
                        break    
                else:
                    print("You are too young to see that film.")

            else:
                print("Please, insert a valid number.")
                
                
    else:
        print("Sorry. We don't have this film.")
        
