import hashlib

def calculate_hash(file_name):
    """Calculate the SHA-1 hash of a file."""
    h = hashlib.sha1()
    
    try:
        with open(file_name, "rb") as file:
            # Read the file in chunks of 1024 bytes
            for chunk in iter(lambda: file.read(1024), b""):
                h.update(chunk)
        return h.hexdigest()
    
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_name}: {e}")
        return None

def compare_files(file_name1, file_name2):
    """Compare two files based on their SHA-1 hash."""
    hash1 = calculate_hash(file_name1)
    hash2 = calculate_hash(file_name2)
    
    if hash1 is None or hash2 is None:
        print("Could not compare files due to an error.")
        return
    
    if hash1 != hash2:
        print("These files are not identical.")
    else:
        print("These files are identical.")

# Example usage
compare_files("PD1.pdf", "PD1.pdf")
