list_J = input()
list_S = input()

result = 0
for element in list_S:
    if element in list_J:
        result = result + 1

print(result)