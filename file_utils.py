import os
import json

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_config(config, filename="config.json"):
    """Save configuration to a JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving config: {str(e)}")
        return False

def load_config(filename="config.json"):
    """Load configuration from a JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading config: {str(e)}")
    return {}

def save_message_to_file(message: str, filename: str) -> bool:
    """Save a message to a file"""
    try:
        with open(filename, 'w') as f:
            f.write(message)
        return True
    except Exception as e:
        print(f"Error saving message: {str(e)}")
        return False

def load_message_from_file(filename: str) -> str:
    """Load a message from a file"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading message: {str(e)}")
        return ""
