from cryptography.fernet import Fernet
import os

# Generate key file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Key generated and saved as secret.key")

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print(f"🔐 Encrypted file saved as: {filename}.encrypted")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_filename = filename.replace(".encrypted", "")

    with open(original_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"🔓 Decrypted file saved as: {original_filename}")

# Menu
if __name__ == "__main__":
    print("🛡️ File Encryption Tool (AES - Fernet)\n")

    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File\n")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        file = input("Enter file name to encrypt: ")
        if os.path.exists(file):
            encrypt_file(file)
        else:
            print("❌ File not found.")

    elif choice == "3":
        file = input("Enter encrypted file name: ")
        if os.path.exists(file):
            decrypt_file(file)
        else:
            print("❌ Encrypted file not found.")

    else:
        print("❌ Invalid choice.")
