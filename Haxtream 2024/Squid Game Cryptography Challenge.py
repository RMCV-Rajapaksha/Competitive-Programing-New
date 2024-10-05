def decrypt_vigenere(ciphertext, keyword):
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    plaintext = []
    for c, k in zip(ciphertext, keyword_repeated):
        if c == ' ':
            plaintext.append(' ')
        else:
            shift = ord(k) - ord('A')
            decrypted_char = chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))
            plaintext.append(decrypted_char)
    return ''.join(plaintext)

def decrypt_transposition(ciphertext):
    num_rows = len(ciphertext) // 5
    if len(ciphertext) % 5 != 0:
        num_rows += 1
    grid = [''] * num_rows
    for i, char in enumerate(ciphertext):
        grid[i % num_rows] += char
    return ''.join(grid)

def decrypt_substitution(ciphertext, key):
    reverse_key = {key[i]: chr(i + ord('A')) for i in range(26)}
    plaintext = ''.join(reverse_key.get(c, c) for c in ciphertext)
    return plaintext

def decrypt_message(substitution_key, encrypted_message):
    # Step 1: Decrypt the modified Vigenere cipher
    intermediate_message_1 = decrypt_vigenere(encrypted_message, "SQUIDGAME")
    
    # Step 2: Decrypt the transposition cipher
    intermediate_message_2 = decrypt_transposition(intermediate_message_1)
    
    # Step 3: Decrypt the substitution cipher
    original_message = decrypt_substitution(intermediate_message_2, substitution_key)
    
    return original_message

# Sample Input
substitution_key =input()
encrypted_message = input()

# Decrypt the message
decrypted_message = decrypt_message(substitution_key, encrypted_message)
print(decrypted_message)