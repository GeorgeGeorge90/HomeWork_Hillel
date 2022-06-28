
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list_copy = lst1[:]

for elem in list_copy:
    if type(elem) != int:
        lst1.remove(elem)

    print('lst2: ', lst1)