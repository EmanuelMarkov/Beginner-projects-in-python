# set is collection which is unordered and unidexed (as well as no duplicate values)
utensils = {"fork","spoon","knife"}
dished ={"bolw","plate","cup"}
utensils.add("cat")
utensils.remove("fork")
utensils.update(dished)
for x in utensils:
    print(x)

dinner_table = utensils.union(dished)
for x in dinner_table:
    print(x)