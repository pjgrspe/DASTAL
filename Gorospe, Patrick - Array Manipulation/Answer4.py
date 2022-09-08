x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]

#Adding 42 and removing numbers 89, 90 and 65
num_to_remove = [89, 90, 65]

x.append(42)
for i in num_to_remove:
    while i in x:
        x.remove(i)

#another option is to use sum() function
sum = 0
for i in x:
    sum = sum + i

print('The sum of all numbers in the array is:',sum)


input('\nPress Enter to continue')