# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import deque
print("Hello world "+ str(20))
str = " number :".join(str(2))
print(str)

lst = [1, 5, 6, 8]
lst1 = [10, 20, 30, 40]
# lst = lst1+lst
lst.extend(lst1)
print(lst)
# lst[:0]=[10]
# /-------------------------
# lst = [10]+lst 
# -------------------------
# lst = deque(lst)
# lst.appendleft(10)
# lst=list(lst)
# ============================
# lst.insert(0, 10)
# print(lst)
# lst[:2]=[100]
# print(lst)
# inx = lst.index(100)
# print(inx)
# lst.remove(100)
# print(lst)
# lst[4:] = [500]
# print(lst)
# lst.pop(0)
# lst[:8] = [50]
# del lst
# print(lst)
# lst.pop()
# print(lst)
del lst[3:5]
print(lst)
# for l in range(len(lst)):
#     print(lst[l], end=" ")
