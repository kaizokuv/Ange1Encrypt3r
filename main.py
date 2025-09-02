import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

def clear_screen():
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            print("\033[3J\033[H\033[2J", end="")
        except Exception:
            os.system("cls")
    else:
        print("\033[3J\033[H\033[2J", end="")

def substitute(text, pattern):
    return ''.join(chr(ord(c) + pattern[i % len(pattern)]) for i, c in enumerate(text))

def reverse_substitute(text, pattern):
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

def encrypt_input(user_input, password, pattern):
    subbed = substitute(user_input, pattern)
    hexed = ''.join(format(ord(c), '02x') for c in subbed)
    encrypted = aes_encrypt(hexed, password)
    return encrypted

def decrypt_input(encrypted_data, password, pattern):
    try:
        hexed = aes_decrypt(encrypted_data, password)
        chars = [chr(int(hexed[i:i+2], 16)) for i in range(0, len(hexed), 2)]
        substituted = ''.join(chars)
        original = reverse_substitute(substituted, pattern)
        return original
    except Exception as e:
        return f"[Error] Decryption failed: {e}"

def menu():
    while True:
        clear_screen()
        print("--- Welcome To The Ange1Encrypt3r ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("> ")
        print("")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            password = input("Enter password (Please Remember This Or You Can't Decrypt ;w; : ")
            pattern = input("Input custom substitution pattern (e.g: +1, -14, +7/enter to leave empty): ")
            if pattern != "":
                try:
                    pattern = [int(x.strip()) for x in pattern.split(",")]
                except:
                    print("Invalid pattern input. Using default.")
                    pattern = [+1, -14, +7, -5, +12]
            else:
                pattern = [+1, -14, +7, -5, +12]
            encrypted = encrypt_input(text, password, pattern)
            print(f"\n[Encrypted]: {encrypted}")

        elif choice == '2':
            enc_text = input("Enter encrypted text: ")
            password = input("Enter password (You Do Remember It? Right..?) : ")
            pattern = input("Input custom substitution pattern (e.g: +1, -14, +7/enter to leave empty): ")
            if pattern != "":
                try:
                    pattern = [int(x.strip()) for x in pattern.split(",")]
                except:
                    print("Invalid pattern input. Using default.")
                    pattern = [+1, -14, +7, -5, +12]
            else:
                pattern = [+1, -14, +7, -5, +12]
            decrypted = decrypt_input(enc_text, password, pattern)
            print(f"\n[Decrypted]: {decrypted}")

        elif choice == '3':
            print("Thanks for using Ange1Encrypt3r!")
            print("Fancy this project? Come check out my other fun stuff at my GitHub at https://github.com/kaizokuv :D")
            break
        else:
            print("")

        again = input("\nDo you want to keep going? (y/n): ")
        if again.lower() != 'y':
            print("")
            print("Thanks for using Ange1Encrypt3r!")
            print("Fancy this project? Come check out my other fun stuff at my GitHub at https://github.com/kaizokuv :D")
            break
            
if __name__ == "__main__":
    menu()