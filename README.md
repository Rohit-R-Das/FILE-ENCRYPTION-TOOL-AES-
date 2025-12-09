# 🔐 File Encryption Tool (AES - Fernet)

A Python-based file encryption and decryption tool using AES (Fernet).  
Beginner-friendly cybersecurity project for understanding cryptography.

## 🚀 Features
- Generate AES encryption key
- Encrypt any file (text, image, PDF, etc.)
- Decrypt encrypted files
- Uses Fernet (AES-128 + HMAC for integrity)

## 🛠 Technologies
- Python 3
- cryptography library (Fernet)

## ▶️ Installation


## 🧪 Example Usage
### 1️⃣ Generate Key
Creates a `secret.key`

### 2️⃣ Encrypt File
Input: `example.txt`  
Output: `example.txt.encrypted`

### 3️⃣ Decrypt File
Input: `example.txt.encrypted`  
Output: `example.txt`

## ⚠️ Important Notes
- Keep `secret.key` safe — without it, decryption is impossible.
- Do not share your key publicly.
