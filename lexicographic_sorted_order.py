# lexicographic_sorted_order
# list1 = input().split()
s = "abc"
r = 2
s = sorted(s)
print(s)
for ltr in s:
    list1 = []
    for ltr1 in s:
        if ltr not in ltr1:
            str1+=str1 + ltr1  
        
        print(str1)
        list1 = []
