import string
import random
from typing import Dict

class EncryptionProgram:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = string.punctuation
        
    def generate_key(self, method: str = "auto") -> str:
        if method == "auto":
            key = str(random.randint(1, 25))
            return key
        elif method == "manual":
            return input("Enter your encryption key (1-25): ")
        else:
            return "13"
    
    def caesar_cipher(self, text: str, key: str, encrypt: bool = True) -> str:
        try:
            shift = int(key) % 26
            if not encrypt:
                shift = -shift
            
            result = ""
            for char in text:
                if char.isalpha():
                    alphabet = self.alphabet_upper if char.isupper() else self.alphabet           
                    position = alphabet.find(char)
                    new_position = (position + shift) % 26
                    result += alphabet[new_position]
                else:
                    result += char
            return result
        except ValueError:
            return "Error: Key must be a number for Caesar cipher"
    

    
    def encrypt_message(self, message: str, key: str = None) -> Dict: # type: ignore
        if key is None:
            key = self.generate_key()
        
        encrypted_text = self.caesar_cipher(message, key, encrypt=True)
        
        return {
            "original": message,
            "encrypted": encrypted_text,
            "key": key,
            "method": "caesar"
        }
    
    def decrypt_message(self, encrypted_message: str, key: str) -> Dict:
        decrypted_text = self.caesar_cipher(encrypted_message, key, encrypt=False)
        
        return {
            "encrypted": encrypted_message,
            "decrypted": decrypted_text,
            "key": key,
            "method": "caesar"
        }

def main():
    program = EncryptionProgram()
    
    print(" ENCRYPTION PROGRAM ")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n--- ENCRYPTION ---")
            message = input("Enter the message to encrypt: ")
            
            print("\nKey generation options:")
            print("1. Auto-generate random key (1-25)")
            print("2. Manual key input (1-25)")
            
            key_choice = input("Choose key option (1-2): ").strip()
            
            if key_choice == "1":
                result = program.encrypt_message(message)
            elif key_choice == "2":
                key = input("Enter your key (1-25): ")
                result = program.encrypt_message(message, key)
            else:
                print("Invalid choice, using auto-generated key")
                result = program.encrypt_message(message)
            
            if "error" not in result:
                print(f"\n ENCRYPTION COMPLETE")
                print(f"Original: {result['original']}")
                print(f"Encrypted: {result['encrypted']}")
                print(f"Key: {result['key']}")
                print(f"Method: {result['method']}")
            else:
                print(f" Error: {result['error']}")
                
        elif choice == "2":
            print("\n--- DECRYPTION ---")
            encrypted_message = input("Enter the encrypted message: ")
            key = input("Enter the decryption key (1-25): ")
            
            result = program.decrypt_message(encrypted_message, key)
            
            if "error" not in result:
                print(f"\n DECRYPTION COMPLETE")
                print(f"Encrypted: {result['encrypted']}")
                print(f"Decrypted: {result['decrypted']}")
                print(f"Method: {result['method']}")
            else:
                print(f" Error: {result['error']}")
                
        elif choice == "3":
            print(" Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":

    main() 
