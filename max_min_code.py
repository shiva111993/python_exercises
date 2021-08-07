print("maximum number:")
l = [90, 300, 10, 3, 60, 1000, 80, 900]
print(l)
# print(len(list))
def max_number(list):
    for i in range(len(list)):
        max = list[i]
        for n in range(1, len(list)):
            if list[n] > max:
                max = list[n]
                inx = list.index(max)
                i = inx
                n = inx+1
    return max
def mini_number(list):
    for i in range(len(list)):
        min = list[i]
        for n in range(1, len(list)):
            if list[n] < min:
                min = list[n]
                inx = list.index(min)
                i = inx
                n = inx+1
    return min
print("find maximum number :", end=" ")
print(max_number(l))
print("find minimum number :", end=" ")
print(mini_number(l))
# if list[0]>list[1]:
#     max = list[0]
# else:
#     max = list[1]
# print(max)