# 🔐 Cryptography and Vehicle Registration System

A simple Python project demonstrating fundamental **cryptography and blockchain-related concepts** through SHA-256 hashing, digital signatures, and a Vehicle Registration System.

The project combines cryptographic operations with a simple vehicle registration and retrieval system.

## 📌 Overview

This project provides the following functionality:

* Generate SHA-256 hashes for messages
* Generate a public-private key pair
* Create digital signatures using a private key
* Verify digital signatures using a public key
* Register vehicle details
* Retrieve vehicle details using a number plate
* Prevent duplicate vehicle number plates
* Validate user menu input

The application uses a menu-driven structure where the menu is displayed repeatedly until the user chooses to exit.

## ✨ Features

### 🔹 SHA-256 Hashing

The system accepts a message from the user and generates its SHA-256 hash.

Example:

```text
Enter a message: Hello Blockchain

SHA-256 Hash:
<64-character hexadecimal hash>
```

SHA-256 is provided using Python's built-in `hashlib` module.

### 🔹 Digital Signature

The project demonstrates digital signatures using an RSA public-private key pair.

The process includes:

1. Generate a private key.
2. Generate the corresponding public key.
3. Accept a message from the user.
4. Sign the message using the private key.
5. Verify the signature using the public key.
6. Display whether the signature is valid or invalid.

Example:

```text
Enter a message to sign: Hello Blockchain

Message signed successfully.

Enter the message to verify: Hello Blockchain

Signature is valid.
```

If the message is modified:

```text
Enter the message to verify: Hello Blockchain Modified

Signature is invalid.
```

### 🔹 Vehicle Registration

The Vehicle Registration System stores:

* Number Plate
* Owner Name
* Vehicle Model

Example:

```text
Number Plate: MH01AB1234
Owner Name: Akshay
Model: Honda City
```

Vehicle information is stored using a Python dictionary.

### 🔹 Vehicle Retrieval

Vehicle details can be retrieved using the number plate.

Example:

```text
Enter Number Plate: MH01AB1234

===== Vehicle Details =====
Number Plate: MH01AB1234
Owner Name: Akshay
Model: Honda City
```

If the number plate does not exist:

```text
Vehicle with this number plate was not found.
```

### 🔹 Duplicate Number Plate Validation

The system prevents multiple vehicles from being registered with the same number plate.

Example:

```text
Enter Number Plate: MH01AB1234
Enter Owner Name: Doremon
Enter Model: Tata Nexon

Vehicle with this number plate already exists.
```

## 📋 Menu

The application provides the following options:

```text
===== Cryptography and Vehicle Registration System =====

1. Generate SHA-256 Hash
2. Generate Digital Signature
3. Verify Digital Signature
4. Register Vehicle
5. Get Vehicle Details
6. Exit
```

## 🛠️ Technologies Used

* **Python 3**
* **SHA-256**
* **RSA**
* **Digital Signatures**
* **Cryptographic Hashing**
* **Object-Oriented / Functional Python**
* **Git & GitHub**

## 📁 Project Structure

```text
Cryptography-Blockchain-Assignment/
│
├── crypto_vehicle.py
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Akshay-Bodhankar/Vehicle-Registration-System.git
```

Navigate to the project directory:

```bash
cd Cryptography-Blockchain-Assignment
```

### 2. Create a Virtual Environment

Creating a virtual environment keeps the project's dependencies isolated from the system Python installation.

#### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

For example:

```text
(venv) $
```

### 3. Upgrade pip

After activating the virtual environment:

```bash
python -m pip install --upgrade pip
```

### 4. Install Required Package

The project uses the `cryptography` package for RSA key generation and digital signatures.

Install it using:

```bash
pip install cryptography
```

Verify the installation:

```bash
pip show cryptography
```

### 5. Run the Project

With the virtual environment activated:

```bash
python crypto_vehicle.py
```

On systems where Python 3 is accessed using `python3`:

```bash
python3 crypto_vehicle.py
```

## 🔑 Cryptography Implementation

### SHA-256

SHA-256 hashing is implemented using Python's `hashlib`:

```python
hashlib.sha256(message.encode()).hexdigest()
```

The resulting hash is a 64-character hexadecimal value.

### RSA Digital Signature

The project uses RSA for public-private key generation.

The private key is used to create the digital signature, while the corresponding public key is used to verify it.

```text
Private Key
     │
     ▼
  Message
     │
     ▼
Digital Signature
     │
     │
     ▼
Public Key + Message
     │
     ▼
Verification
     │
 ┌───┴────┐
 ▼        ▼
Valid   Invalid
```

## 🚗 Vehicle Data Structure

Vehicle information is stored in a dictionary using the number plate as the key.

Example:

```python
vehicles = {
    "MH01AB1234": {
        "owner": "Akshay",
        "model": "Honda City"
    }
}
```

This allows vehicle details to be retrieved directly using the number plate.

## 🧪 Test Cases

### SHA-256 Hash

```text
Input:
Hello Blockchain

Expected:
64-character SHA-256 hash
```

### Digital Signature

Sign:

```text
Hello Blockchain
```

Verify:

```text
Hello Blockchain
```

Expected:

```text
Signature is valid.
```

Modify the message:

```text
Hello Blockchain Modified
```

Expected:

```text
Signature is invalid.
```

### Vehicle Registration

Input:

```text
Number Plate: MH01AB1234
Owner: Akshay
Model: Honda City
```

Expected:

```text
Vehicle registered successfully.
```

### Duplicate Number Plate

Register the same number plate again:

```text
MH01AB1234
```

Expected:

```text
Vehicle with this number plate already exists.
```

### Vehicle Retrieval

Input:

```text
MH01AB1234
```

Expected:

```text
Number Plate: MH01AB1234
Owner Name: Akshay
Model: Honda City
```

### Vehicle Not Found

Input:

```text
MH99ZZ9999
```

Expected:

```text
Vehicle with this number plate was not found.
```

## ⚠️ Project Scope

This project is intended for **educational purposes** and demonstrates fundamental concepts related to cryptography and blockchain.

It is not intended to be used as a production-ready vehicle registration or identity-management system.

## 🎯 Learning Objectives

This project demonstrates:

* SHA-256 cryptographic hashing
* Public-key cryptography
* RSA key generation
* Digital signature creation
* Digital signature verification
* Message integrity
* Vehicle data storage and retrieval
* Input validation
* Menu-driven application design
* Python virtual environments and package management

## 📚 Assignment Requirements

The implementation covers the following requirements:

* SHA-256 hash generation
* Digital signature generation
* Public-private key pair
* Digital signature verification
* Vehicle registration
* Vehicle retrieval by number plate
* Owner and model information
* Duplicate number-plate validation
* Menu-driven application

## 👨‍💻 Author

**Akshay Bodhankar**

GitHub: `https://github.com/Akshay-Bodhankar`

---

⭐ If you found this project useful, consider giving the repository a star!
