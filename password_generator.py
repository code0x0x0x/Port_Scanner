import random
import string
import argparse

def is_password_compromised(password):
    """
    Check if the password is in a list of common compromised passwords (simplified for demo).
    In a real-world scenario, integrate with APIs like "Have I Been Pwned".
    """
    common_passwords = {"password", "123456", "qwerty", "admin"}
    return password in common_passwords

def evaluate_password_strength(password):
    """
    Evaluate the strength of a password based on length and character diversity.
    Returns a strength rating (weak, medium, strong).
    """
    if len(password) < 8:
        return "weak"
    elif len(password) < 12:
        return "medium"
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        if has_upper and has_lower and has_digit and has_special:
            return "strong"
        else:
            return "medium"

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """
    Generate a secure password with customizable character sets.

    Args:
        length (int): Length of the password. Default is 12.
        use_uppercase (bool): Include uppercase letters. Default is True.
        use_lowercase (bool): Include lowercase letters. Default is True.
        use_numbers (bool): Include numbers. Default is True.
        use_special (bool): Include special characters. Default is True.

    Returns:
        str: Generated password.
    """
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if not is_password_compromised(password):
            break

    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password with customizable options.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--strength", type=str, choices=["weak", "medium", "strong"], default="strong",
                      help="Desired password strength (default: strong)")
    
    args = parser.parse_args()
    
    # Adjust character sets based on strength
    use_uppercase = args.strength in ["medium", "strong"]
    use_lowercase = args.strength in ["medium", "strong"]
    use_numbers = args.strength in ["medium", "strong"]
    use_special = args.strength == "strong"
    
    password = generate_password(
        length=args.length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_special=use_special
    )
    
    print("Generated Password:", password)
    print("Strength:", evaluate_password_strength(password))
    print("Note: For secure storage, use strong encryption like argon2 or PBKDF2.")
    print("Note: Enable Multi-Factor Authentication (MFA) for added security.")

if __name__ == "__main__":
    main() 
