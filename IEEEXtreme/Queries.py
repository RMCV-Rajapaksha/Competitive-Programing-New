def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read N and Q
    N, Q = map(int, data[0].split())
    
    # Read permutation P
    P = list(map(int, data[1].split()))
    
    # Initialize A with zeros
    A = [0] * N
    
    # Prepare the output list
    output = []
    
    # Process each query
    for i in range(2, 2 + Q):
        query = list(map(int, data[i].split()))
        T = query[0]
        
        if T == 0:
            # Type 0 update
            l, r, c = query[1] - 1, query[2] - 1, query[3]
            for j in range(l, r + 1):
                A[j] += c
        
        elif T == 1:
            # Type 1 update
            l, r, c = query[1] - 1, query[2] - 1, query[3]
            for j in range(l, r + 1):
                A[P[j] - 1] += c
        
        elif T == 2:
            # Type 2 query
            l, r = query[1] - 1, query[2] - 1
            result = sum(A[l:r + 1])
            output.append(result)
        
        elif T == 3:
            # Type 3 query
            l, r = query[1] - 1, query[2] - 1
            result = sum(A[P[j] - 1] for j in range(l, r + 1))
            output.append(result)
    
    # Print all results for type 2 and type 3 queries
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

if __name__ == "__main__":
    main()