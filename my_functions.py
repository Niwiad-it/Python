from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def encrypt_message(public_key_pem: str, message: str) -> str:
    """
    Encrypt a message using RSA public key
    Returns the encrypted message as a base64 string
    """
    try:
        # Convert PEM string to public key object
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode()
        )
        
        # Encrypt the message
        encrypted = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Convert to base64 for easier handling
        return base64.b64encode(encrypted).decode()
    except Exception as e:
        raise Exception(f"Encryption error: {str(e)}")

def decrypt_message(private_key_pem: str, encrypted_message: str) -> str:
    """
    Decrypt a message using RSA private key
    Returns the decrypted message as a string
    """
    try:
        # Convert PEM string to private key object
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None
        )
        
        # Decode from base64
        encrypted = base64.b64decode(encrypted_message.encode())
        
        # Decrypt the message
        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode()
    except Exception as e:
        raise Exception(f"Decryption error: {str(e)}")

def save_message_to_file(message: str, filename: str) -> bool:
    """
    Save an encrypted or decrypted message to a file
    Returns True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as f:
            f.write(message)
        return True
    except Exception:
        return False

def load_message_from_file(filename: str) -> str:
    """
    Load an encrypted or decrypted message from a file
    Returns the message as a string
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        raise Exception(f"Failed to load message: {str(e)}")