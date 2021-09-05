n = int(input())
matrix = []
result_values = []
for i in range(0, n):
    inp = map(int, input().split())
    matrix.extend(inp)

for i in range(0, n):
    calc = None
    for j in range(i + 1, n):
        val = matrix[i * n + j]
        if calc is None:
            calc = val
        else:
            calc = calc | val
    for j in range(0, i):
        val = matrix[j * n + i]
        if calc is None:
            calc = val
        else:
            calc = calc | val
    if calc is None:
        calc = 0
    result_values.append(str(calc))

print(" ".join(result_values))

