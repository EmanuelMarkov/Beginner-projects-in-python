a = [1, 1, 4, 3, 5, 8, 13, 21, 34, 55, 89]

b = [i for i in a if i < 5]
print(b)

number_to_check = int(input("Tell me a number to check? :"))

c = [i for i in a if i < number_to_check]
print(c)




