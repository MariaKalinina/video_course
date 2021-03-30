my_list = [2, 5, 8, 2, 3, 12, 12]
new_list = []
for n in my_list:
    n_amount = my_list.count(n)
    if n_amount == 1:
        new_list.append(n)
print(new_list)
