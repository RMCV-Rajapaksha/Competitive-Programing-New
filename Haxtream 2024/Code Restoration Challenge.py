def can_restore_code(A, B):
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] == 'S' and i + 1 < len(A) and A[i + 1] == 'S' and B[j] == 'T':
            i += 2
            j += 1
        else:
            return False
    return i == len(A) and j == len(B)

def main():
    N = int(input())
    for _ in range(N):
        A, B = input().split()
        result = can_restore_code(A, B)
        print("True" if result else "False")

if __name__ == "__main__":
    main()
    