from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from typing import Tuple

def generate_new_keypair(key_size: int = 2048) -> Tuple[str, str]:
    """Generate a new RSA key pair with the specified key size."""
    try:
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        
        # Get public key
        public_key = private_key.public_key()
        
        # Serialize private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        # Serialize public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return public_pem.decode(), private_pem.decode()
    except Exception as e:
        raise Exception(f"Failed to generate key pair: {str(e)}")

def save_keys_to_file(public_key: str, private_key: str, 
                     public_file: str = "public_key.pem", 
                     private_file: str = "private_key.pem") -> None:
    """Save the key pair to files."""
    try:
        with open(public_file, 'w') as f:
            f.write(public_key)
        
        with open(private_file, 'w') as f:
            f.write(private_key)
    except Exception as e:
        raise Exception(f"Failed to save keys: {str(e)}")

def load_keys_from_file(public_file: str = "public_key.pem", 
                       private_file: str = "private_key.pem") -> Tuple[str, str]:
    """Load the key pair from files."""
    try:
        with open(public_file, 'r') as f:
            public_key = f.read()
        
        with open(private_file, 'r') as f:
            private_key = f.read()
        
        return public_key, private_key
    except Exception as e:
        raise Exception(f"Failed to load keys: {str(e)}")
