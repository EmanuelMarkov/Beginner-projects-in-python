rows = int(input("Input the number of rows "))
colums = int(input("Input the number of colums "))
symbol = input("Write down ur symbol ")

for i in range(rows):
    for j in range(colums):
        print(symbol,end="")
    print()
