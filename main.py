from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

pattern = [+1, -14, +7, -5, +12]

def substitute(text):
    return ''.join(chr(ord(c) + pattern[i % len(pattern)]) for i, c in enumerate(text))

def reverse_substitute(text):
    return ''.join(chr(ord(c) - pattern[i % len(pattern)]) for i, c in enumerate(text))

def get_aes_key(password):
    return hashlib.sha256(password.encode()).digest()

def aes_encrypt(hex_text, password):
    key = get_aes_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(hex_text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def aes_decrypt(b64_data, password):
    try:
        key = get_aes_key(password)
        raw = base64.b64decode(b64_data)
        iv = raw[:16]
        ct = raw[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ct)
        return unpad(decrypted, AES.block_size).decode()
    except Exception as e:
        raise Exception(f"AES decryption error: {e}")

def encrypt_input(user_input, password):
    subbed = substitute(user_input)
    hexed = ''.join(format(ord(c), '02x') for c in subbed)
    encrypted = aes_encrypt(hexed, password)
    return encrypted

def decrypt_input(encrypted_data, password):
    try:
        hexed = aes_decrypt(encrypted_data, password)
        chars = [chr(int(hexed[i:i+2], 16)) for i in range(0, len(hexed), 2)]
        substituted = ''.join(chars)
        original = reverse_substitute(substituted)
        return original
    except Exception as e:
        return f"[Error] Decryption failed: {e}"

def menu():
    while True:
        print("\n--- Welcome To The Ange1Encrypt3r ---")
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("\nChoose your option: ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            password = input("Enter password (Please Remember This Or You Can't Decrypt ;w; : ")
            encrypted = encrypt_input(text, password)
            print(f"\n[Encrypted]: {encrypted}")

        elif choice == '2':
            enc_text = input("Enter encrypted text: ")
            password = input("Enter password (You Do Remember It? Right..?) : ")
            decrypted = decrypt_input(enc_text, password)
            print(f"\n[Decrypted]: {decrypted}")

        elif choice == '3':
            print("Thanks for using Ange1Encrypt3r!")
            print("Fancy this project? Come check out my other fun stuff at my GitHub at https://github.com/kaizokuv :D")
            break
        else:
            print("Sorry mate, but that ain't an option, try again yeah?")

        again = input("\nDo you want to keep going? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for using Ange1Encrypt3r!")
            print("Fancy this project? Come check out my other fun stuff at my GitHub at https://github.com/kaizokuv :D")
            break
            
if __name__ == "__main__":
    menu()

