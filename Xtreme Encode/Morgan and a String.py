def morganAndString():
    for test in range(int(input())):
        a, b = (input() + 'z' for line in range(2))
        i = j = 0
        result = ''
        while not a[i] == b[j] == 'z':
            if a[i:] < b[j:]:
                result += a[i]
                i += 1
            else:
                result += b[j]
                j += 1
        print(result)

if __name__ == '__main__':
    morganAndString()