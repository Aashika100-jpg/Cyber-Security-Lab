def encrypt(text, key):
    result = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')        # convert to 0-25
            c = (p + key) % 26              # encryption formula
            result += chr(c + ord('A'))     # back to letter
        else:
            result += char
    return result


def decrypt(cipher, key):
    result = ""
    for char in cipher.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (c - key) % 26              # decryption formula
            result += chr(p + ord('A'))
        else:
            result += char
    return result


# Example
text = "HELLO"
key = 3

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
