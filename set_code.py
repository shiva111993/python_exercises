# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# myset = {"apple", "ball", "cat", "dag", "elephate"}
# print(myset)
# myset.add("fan")
# print(myset)
# myset.add("apple")
# print(myset)
# ---------removing
# myset.remove("ball")
# print(myset)
# myset.discard("apple")
# print(myset)
# myset.pop()
# print(myset)
# myset.clear()
# print(myset)
# del myset
# print(myset)
# ------------------loop
# for x in myset:
#     print(x)
# ------------------ adding & update
# myset2 = {"car", "bike", "cycle"}
# myset3 = {False, True, False, False, True}
# myset4 = {1, 2, 3, 4, 5}
# mylist = ["kiwi", "orange"]
# myset.update(myset2, myset3, myset4, mylist)
# print(myset)
# print("kiwi" in myset)
# ------------------ join set
# myset = {"a", "b", "c"}
# myset2 = {"a", "b", "c", "d"} 

# myset3 = {1, 2, 3}
# myset3 = myset.union(myset2)
# print(myset3)
# --intersection and intersection_update
# set1 = {"apple","banana","carry"}
# set2 = {"google","microsoft","apple"}
# intersction
# set3 = set1.intersection(set2)
# print(set3)
# interction_update
# set1.intersection_update(set2)
# print(set1)
# --symmetric_difference_update()  & symmetric_difference()
# method will keep only the elements that are NOT present in both sets.
# Keep All, But NOT the Duplicates
# set1 = {"apple","banana","carry"}
# set2 = {"google","microsoft","apple"}
# set1.symmetric_difference(set2) #it not work
# set3 = set1.symmetric_difference(set2)#o/p:-{'microsoft', 'banana', 'google', 'carry'}
# print(set3)
# set1.symmetric_difference_update(set2)
# print(set1)
# --issubset()
# set1= {"a","b","c"}
# set2 = {"f", "e", "d", "a","b","c"}
# set3 =  set1.issubset(set2)
# print(set3)
# --issuperset()
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y) 
# print(z)
# --isdisjoin() 
# Return True if no items in set x is present in set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# #  -------------- or -------------
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z =  x.isdisjoint(y)
# print(z)
