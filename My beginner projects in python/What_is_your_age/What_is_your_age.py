import datetime

name = input("Hi, What is your name? ")
age = int(input("And how old were you again? "))
current_year =int (datetime.datetime.now().year)
turn_100 = current_year + (100-age)
print("Hi " + name + " you will turn 100 in the year " +  str(turn_100))

annoy = int(input("So how much times do you want to hear that "))
while annoy>0:
    print("Hi " + name + " you will turn 100 in the year " +  str(turn_100) + "\n")
    annoy -= 1