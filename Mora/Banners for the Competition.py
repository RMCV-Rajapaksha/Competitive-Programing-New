n = int(input().strip())
s = input().strip()
m = int(input().strip())
t = [input().strip() for _ in range(m)]

if m not in [1, 2, 3] or len(s) != n or any(len(h) != n for h in t):
    print(-1)
    exit()

if not s.isalpha() or not s.islower():
    print(-1)
    exit()
for h in t:
    if len(h) != len(s) or not h.isalpha() or not h.islower():
        print(-1)
        exit()

n = len(s)
total_o = 0

for i in range(n):
    c = set(h[i] for h in t)
    c.add(s[i])

    if len(c) == 1:
        continue

    min_ops = float('inf')
    for target in c:
        o = sum(min((ord(target) - ord(char)) % 26, (ord(char) - ord(target)) % 26) for char in c)
        min_ops = min(min_ops, o)

    total_o += min_ops

print(total_o)