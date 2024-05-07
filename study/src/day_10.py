numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

new_ls = [ i for i in numbers if i <= 0]

print(new_ls)


my_list = [[1, 2], [3, 4]]
my_list = [item for sublist in my_list for item in sublist]
print(my_list)