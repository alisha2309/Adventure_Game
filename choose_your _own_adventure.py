name=input("Enter you name: ")
print("Welcome ",name," to this adventure!" )

answer=input("You ar on a dirt road, it has come to an end!! Choose the way LEFT / RIGHT.").lower()

if answer == "left":
    answer=input("River ahead!! Choose Swim / Walk.").lower()
    
    if answer== "swim":
        print("Eaten by alligator !! You lost!!")
       
    elif answer == "walk":
        print("Lost the path!! You lost!!")
    else:
        print("Enter a valid option")
     
elif answer== "right":
    answer=input("Bridge ahead!! Choose cross/back.").lower()
    if answer=="back":
        print("You go back and lost the game")
    elif answer=="cross":
        answer=input("You crossed the bridge and met the stranger!! Do you want to talk? yes / no").lower()

        if answer == "yes":
            print("The stranger gave you a key to the palace. You Win!! Congtrats!!")

        elif answer =="no":
            print("You Lost the game")
        else:
            print("Enter a valid option")
else:
    print("Enter a valid option.")

print("Thank you for playing the game", name)