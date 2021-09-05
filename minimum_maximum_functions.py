def minimum(obj):
    #pos1 means position 1
    #pos2 means position 2
    print("finding minimum number in List")
    pos1 = 0 
    for pos2 in range(1, len(obj)):
        # print(pos1)
        if list[pos1] < list[pos2]:
            min = list[pos1]
        else:
            min = list[pos2]
            pos1 = pos2
            pos2 += 1
    return min
def maximum(obj):
    #pos1 means position 1
    #pos2 means position 2
    print("finding maximum number in List")
    pos1 = 0 
    for pos2 in range(1, len(obj)):
        # print(pos1)
        if list[pos1] > list[pos2]:
            min = list[pos1]
        else:
            min = list[pos2]
            pos1 = pos2
            pos2 += 1
    return min
    
list = [5, 6, 8, -3, 9, 10, 1, 0, -1, -4]
# list = [5, 6]
print(list)
print("minimum number:", minimum(list))
print("maximun number:", maximum(list))