x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
y = [1, 2, 3]

number_input = input('Input number: ')
array_input = input('Input arr: ')


if array_input == 'x':
    counter = x.count(int(number_input))
    print('Number of occurences of', number_input, 'in array', array_input,'is:', counter)
elif array_input == 'y':
    counter = y.count(int(number_input))
    print('Number of occurences of', number_input, 'in array', array_input,'is:', counter)
else:
    print('Array does not exist')


input()