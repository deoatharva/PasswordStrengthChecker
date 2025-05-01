import re

def check_password_strength(password):
    """
    Function to check the strength of a password.
    """
    if len(password) < 12:
        return "Weak: Password must be at least 12 characters long"
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number"
        
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase"
        
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password strong"
    
    return "Strong: Your password is secure!"

def password_checker():
    """
    Main function to take user input and check password strength.
    """
    print("Welcome to the Password Strength Checker")
    
    while True:
        password = input("\nEnter your password: ")
        
        if password.lower() == "exit":
            print("Thank you")
            break
        
        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    password_checker()
