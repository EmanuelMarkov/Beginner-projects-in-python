import math

exit_prompt = ""

while exit_prompt == (""):

    number = float(input("Give me a number and I will tell you if its even or odd: "))
    if number%4 == 0:
        print("This number is even and devisible by 4")
      

    elif number%2==0:
        print("even")
    else:
        print("odd")

    exit_prompt = input("Press enter if you wish to continue, press anything else to exit \n")

continue_option = input("Since you are already here lets try one more thing, do you wish to try? y/n :")

while continue_option=="y": 
      
      number_to_check = int(input("Give me a number to check! "))
      number_to_divide = int(input("Now give me number to divide by: "))
      if number_to_check%number_to_divide==0:
          print("Yep they divide")
      else:
        print("Sorry they dont divide")
      continue_option = input("Wanna keep going? y/n :")
  



print("Bye bye")
        





          

