s = input().strip()

arr = []
for i in s:
    if i.isdigit():
        arr.append(int(i))
    else:
        b = arr.pop()
        a = arr.pop()
        if i == '+':
            arr.append(a+b)
        elif i == '-':
            arr.append(a-b)
        elif i == '*':
            arr.append(a*b)
        elif i == '/':
            arr.append(a//b)     

print(arr[0])