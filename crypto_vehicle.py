import hashlib

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, _serialization
from cryptography.hazmat.primitives.asymmetric import padding

vehicles = {}

def generate_hash(message):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    return hash_value

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 2048
    )

    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length = padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return True
    except Exception:
        return False


def register_vehicle(number_plate, owner_name, model):
    if number_plate in vehicles:
        print("Vehicle with this number plate is already Exists.")
        return False

    vehicles[number_plate] = {
        "owner": owner_name,
        "model": model
    }
    print(f"Vehicle with number plate {number_plate} registered successfully.")
    return True

def get_vehicle(number_plate):
    if number_plate not in vehicles:
        print("Vehicle with this number plate does not exist.")
        return False

    vehicle = vehicles[number_plate]
    print("\n=====Vehicle Details=====")
    print(f"Number Plate: {number_plate}")
    print(f"Owner Name: {vehicle['owner']}")
    print(f"Model: {vehicle['model']}")

    return True


if __name__ == "__main__":

    private_key, public_key = generate_keys()
    signature = None

    while True:
        print("\n=====Cryptography and Vehicle Registration System=====")
        print("1. Generate SHA256 Hash")
        print("2. Generate Digital Signature")
        print("3. Verify Digital Signature")
        print("4. Register Vehicle")
        print("5. Get Vehicle Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            message = input("Enter a message: ")
            hash_value = generate_hash(message)
            print("\nSHA256 Hash: ")
            print(hash_value)

        elif choice == "2":
            message = input("Enter a message to sign: ")
            signature = sign_message(private_key, message)
            print("\nMessage signed successfully.")
            print("Digital Signature: ")
            print(signature.hex())

        elif choice == "3":
            if signature is None:
                print("\nNo signature has been generated yet. Please generate a signature first.")

            else:
                message = input("Enter the message to verify: ")

                is_valid = verify_signature(public_key, message, signature)
                
                if is_valid:
                    print("\nSignature is valid.")
                else:
                    print("\nSignature is invalid.")

            
        elif choice == "4":
            number_plate = input("Enter vehicle number plate: ")
            owner_name = input("Enter owner name: ")
            model = input("Enter the vehicle model: ")

            register_vehicle(number_plate, owner_name, model)

        elif choice == "5":
            number_plate = input("Enter vehicle number plate: ")
            get_vehicle(number_plate)

        elif choice == "6":
            print("\nExiting...")
            break

        else:
            print("\nInvalid choice. Please try again.")