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

    number_plate = input("Enter vehicle number plate: ")
    owner_name = input("Enter Owners name: ")
    model = input("Enter vehicle model: ")

    register_vehicle(number_plate, owner_name, model)
    register_vehicle(number_plate, owner_name, model)

    get_vehicle(number_plate)


    # private_key, public_key = generate_keys()

    # message = input("Enter a message to sign: ")

    # signature = sign_message(private_key, message)

    # print("\nMessage signed successfully!")

    # is_valid = verify_signature(public_key, message, signature)

    # if is_valid:
    #     print("SIgnature is valid")
    # else:
    #     print("Signature is invalid")