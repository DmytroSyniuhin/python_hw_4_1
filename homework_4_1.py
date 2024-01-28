list_1 = [0, 1, 0, 12, 3]
count_1 = 1
while count_1 <= list_1.count(0):
    list_1.pop(list_1.index(0))
    list_1.append(0)
    count_1 += 1
print(list_1)


list_2 = [0]
count_2 = 1
while count_2 <= list_2.count(0):
    list_2.pop(list_2.index(0))
    list_2.append(0)
    count_2 += 1
print(list_2)


list_3 = [1, 0, 13, 0, 0, 0, 5]
count_3 = 1
while count_3 <= list_3.count(0):
    list_3.pop(list_3.index(0))
    list_3.append(0)
    count_3 += 1
print(list_3)


list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
count_4 = 1
while count_4 <= list_4.count(0):
    list_4.pop(list_4.index(0))
    list_4.append(0)
    count_4 += 1
print(list_4)
