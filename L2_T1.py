my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list_1_new = []
for n in my_list_1:
    if n not in my_list_1_new:
        my_list_1_new.append(n)
for i in my_list_1_new:
    if i in my_list_2:
        my_list_1_new.remove(i)
print(my_list_1_new)
