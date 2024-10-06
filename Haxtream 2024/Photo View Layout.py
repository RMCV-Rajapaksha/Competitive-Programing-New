def arrange_photos(n, photos):
    rows = 0  # To count the number of rows
    i = 0     # Pointer to traverse the list of photos
    
    while i < n:
        # Case 1: Three Portraits (P P P)
        if i + 2 < n and photos[i] == 'P' and photos[i+1] == 'P' and photos[i+2] == 'P':
            rows += 1
            i += 3  # Move pointer by 3 positions
            
        # Case 2: Two Landscapes (L L)
        elif i + 1 < n and photos[i] == 'L' and photos[i+1] == 'L':
            rows += 1
            i += 2  # Move pointer by 2 positions
        
        # Case 3: Two Portraits and One Landscape (P P L / L P P / P L P)
        elif i + 2 < n:
            if (photos[i] == 'P' and photos[i+1] == 'P' and photos[i+2] == 'L') or \
               (photos[i] == 'L' and photos[i+1] == 'P' and photos[i+2] == 'P') or \
               (photos[i] == 'P' and photos[i+1] == 'L' and photos[i+2] == 'P'):
                rows += 1
                i += 3  # Move pointer by 3 positions
        
        # Case 4: One Portrait and One Landscape (P L / L P)
        elif i + 1 < n:
            rows += 1
            i += 2  # Move pointer by 2 positions
        
        # Case 5: Remaining incomplete row
        else:
            rows += 1
            i += 1  # Move pointer by 1 (incomplete row)
    
    return rows

# Input handling
n = int(input())  # Number of images
photos = input().split()  # List of photos (either 'P' or 'L')

# Solve the problem
result = arrange_photos(n, photos)
print(result)
