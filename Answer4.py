x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
num_to_remove = [89, 90, 65]

x.append(42)
for i in num_to_remove:
    while i in x:
        x.remove(i)

print('The sum of all numbers in array is:',sum(x))

input()