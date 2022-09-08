x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
y = [0, 1, 1, 2, 3, 4, 3, 1, 2, 4]

#asking for user input
number_input = input('Input number: ')
array_input = input('Input array: ')

#else if statements
if array_input == 'x':
    counter = x.count(int(number_input))
    print('Number of occurences of', number_input, 'in array', array_input,'is:', counter)
elif array_input == 'y':
    counter = y.count(int(number_input))
    print('Number of occurences of', number_input, 'in array', array_input,'is:', counter)
else:
    print('Array does not exist')


input('\nPress Enter to continue')