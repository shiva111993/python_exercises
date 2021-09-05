from itertools import permutations
list1 = input().split()
s = sorted(list1[0])
r = int(list1[1])
# print(sorted(find[0]))
list2=list(permutations(s,r)
# print(type(list1[1]))
# print(len(list1))
for pos in range(len(list2)):
    ltr1 = ""
    for ltr in list2[pos]:
        ltr1 += ltr
    print(ltr1)