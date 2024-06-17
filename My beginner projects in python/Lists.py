food = ["pizza","tacos","ice cream","pudding"]
food[0]="sushi"
print(food[3])
print()
for x in food:
    print(x)

food.append("bao buns")
food.remove("pudding")
food.insert("cake")
food.sort()

for x in food:
    print(x)

food.clear()

