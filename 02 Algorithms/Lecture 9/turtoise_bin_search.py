v, d = map(int, input().split())
n = int(input())
ans = 0
curr_pos = 0
curr_time = 0
for i in range(n):
    d, s = input().split()
    d = int(d)
    s = list(map(int, s.split(":")))
    t = s[0] * 60 + s[1]
    ans += (d - curr_pos) / v
    if t < ans:
        ans = t
    ans += d
ans += d / v
print(ans)
