n = int(input().strip())
s = input().strip()
m = int(input().strip())
themes = [input().strip() for _ in range(m)]

if m not in [1, 2, 3] or len(s) != n or any(len(theme) != n for theme in themes):
    print(-1)
    exit()

if not s.isalpha() or not s.islower():
    print(-1)
    exit()
for theme in themes:
    if len(theme) != len(s) or not theme.isalpha() or not theme.islower():
        print(-1)
        exit()

n = len(s)
total_o = 0

for i in range(n):
    c = set(theme[i] for theme in themes)
    c.add(s[i])

    if len(c) == 1:
        continue

    min = float('inf')
    for target in c:
        o = sum(min((ord(target) - ord(char)) % 26, (ord(char) - ord(target)) % 26) for char in c)
        min = min(m, o)

    total_o += min

print(total_o)