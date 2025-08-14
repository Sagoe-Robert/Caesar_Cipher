### Caesar Cipher Encryption Program

### Overview
Interactive Python CLI **(Command-Line Interface)** that encrypts and decrypts text using the Caesar cipher.

### Features
- **Caesar cipher only**
- **Numeric keys 1–25**
- **Auto-generate key** or **enter manually**
- Preserves case; non-letters (digits, spaces, punctuation) are unchanged

### Requirements
- Python 3.7+

### Run
```bash
python encryption_program.py
# On some Windows setups:
py encryption_program.py
```

### Usage
1. Choose: 1) Encrypt, 2) Decrypt, 3) Exit
2. For encrypt:
   - Enter the message
   - Choose key option: auto (random 1–25) or manual (enter 1–25)
   - The program prints the encrypted text and the key used
3. For decrypt:
   - Enter the encrypted text
   - Enter the key (same number used to encrypt)

### Examples
Encrypt with manual key 3:
```text
Enter the message to encrypt: Hello, World!
Choose key option (1-2): 2
Enter your key (1-25): 3
Encrypted: Khoor, Zruog!
Key: 3
```

Decrypt with key 3:
```text
Enter the encrypted message: Khoor, Zruog!
Enter the decryption key (1-25): 3
Decrypted: Hello, World!
```

### Notes
- Valid keys are integers in the range 1–25
- Use the same key for decryption that was used for encryption
