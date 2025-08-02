###练习###
#练习1
car = input("What kind of car do you want to rent? "
            "\nPlease tell me: ")
print(f"Let me see if I can find you a {car.title()}. @^_^@")
#练习2
peo_number = input("Excuse me, how many people do you have for dinner? "
                   "\nTell me: ")
peo_number = int(peo_number)
if peo_number >= 8:
    print("Sorry,we don't have a free table.")
else:
    print("OK,we have a free table.")
#练习3
number = input("Enter a number for me and I can "
               "tell you if it is a multiple of 10. ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10. ")
else:
    print(f"The number {number} is not a multiple of 10. ")
#练习4
prompt = "\nPlease enter the pizza toppings you want to add : "
prompt += "\n(Enter 'quit' to stop prodution.) "
message = ''
while message != 'quit':
    message = input(prompt)
    if message =='quit':
        break
    else:
        print(f"Okay,add toppings {message} to the pizza!")
#练习5
while True:
    age = input("\nPlease tell me your age(enter 'quit' to exit)"
            "\n I will show you the fare: ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free. ")
        elif age >= 12:
            print("You ticket is $ 10. ")
        else:
            print("Your ticket is $ 15. ")
