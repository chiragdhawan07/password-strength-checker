import string

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "❗ Password should be at least 8 characters long.\n"

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        remarks += "❗ Add lowercase letters.\n"

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks += "❗ Add uppercase letters.\n"

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks += "❗ Add digits.\n"

    # Check for special characters
    special_characters = string.punctuation
    if any(char in special_characters for char in password):
        strength += 1
    else:
        remarks += "❗ Add special characters (e.g. @, #, $, !).\n"

    # Determine strength level
    if strength == 5:
        return "✅ Strong Password!"
    elif 3 <= strength < 5:
        return f"⚠️ Medium Strength Password.\n{remarks}"
    else:
        return f"❌ Weak Password.\n{remarks}"


# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("🔐 Password Strength Checker\n")
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("\nResult:")
    print(result)
