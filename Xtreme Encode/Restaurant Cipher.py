def find_recipe(secret_messages):
    for message in secret_messages:
        # Initialize a dictionary to keep track of counts for each letter A-G
        letter_count = {letter: 0 for letter in 'ABCDEFG'}
        
        # Count the occurrences of each relevant letter in the message
        for char in message:
            if char.upper() in letter_count:
                letter_count[char.upper()] += 1
        
        # Find the letter with the maximum count
        max_letter = max(letter_count, key=letter_count.get)
        print(max_letter)

if __name__ == "__main__":
    # Input the number of secret messages
    n = int(input())
    
    # Input each secret message
    secret_messages = []
    for _ in range(n):
        secret_messages.append(input())
    
    # Find and output the recipe letter for each secret message
    find_recipe(secret_messages)