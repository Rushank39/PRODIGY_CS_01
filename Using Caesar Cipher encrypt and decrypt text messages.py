# Caesar Cipher Implementation

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within the bounds of A-Z or a-z
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
if __name__ == "__main__":
    print("Caesar Cipher Tool")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")
