
V, E = map(int, input().split())
e_list = []
result = "NO"
for _ in range(E):
    current = list(map(int, input().split()))
    if current in e_list:
        result = "YES"
    e_list.append(current)

print(result)
