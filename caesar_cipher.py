def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Determine if we're encrypting or decrypting
    if mode == 'decrypt':
        shift = -shift
    
    # Process each character in the text
    for char in text:
        if char.isalpha():
            # Determine the starting ASCII value (A=65, a=97)
            start = ord('A') if char.isupper() else ord('a')
            
            # Apply the shift and wrap around the alphabet
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    encrypted = caesar_cipher(message, shift, 'encrypt')
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()