def encrypt(text, key):
    if key > 10000:
        print("The key is too big! (maximum key is 10000)")
        return text
    else:
        min_char = 32
        max_char = 95

        encrypt_char = lambda char: chr((ord(char) + key - min_char) % max_char + min_char)
        encrypted_text = ''.join(map(encrypt_char, text))

        return encrypted_text

def decrypt(text, key):
    if key > 10000:
        print("The key is too big! (maximum key is 10000)")
        return text
    else:
        min_char = 32
        max_char = 95
        makePositive = 10000 * 95

        decrypt_char = lambda char: chr((ord(char) - key - min_char + makePositive) % max_char + min_char)
        decrypted_text = ''.join(map(decrypt_char, text))       

        return decrypted_text

text = "Hello,World!"
key = 42

encrypted_text = encrypt(text, key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
