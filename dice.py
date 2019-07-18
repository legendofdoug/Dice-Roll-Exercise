import random
check = "yes"
while check.lower() != "no":
    print ("Rolling this bitch!")
    rolled_num =  random.randint(1,6)
    print ("You rolled a", rolled_num)
    check = input("Would you like to roll again? yes/no \n")
    while check.lower() != "no" and check.lower() != "yes":
        print("Please type 'yes' or 'no'.")
        check = input("Would you like to roll again? yes/no \n")
