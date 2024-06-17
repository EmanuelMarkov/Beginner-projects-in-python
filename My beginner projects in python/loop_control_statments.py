while True:
    name=input("Enetr your name ")
    if name != "":
        break

phone_number  = "123-456-789"

for i in phone_number:
    if i =="-":
        continue
    print(i,end="")

print()

for i in range (1,21):
    if i == 13:
        pass
    else:
        print(str(i) + " ",end="")