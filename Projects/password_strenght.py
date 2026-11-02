#EH CP1 Password strenght checker

password = input("Enter a password: ")

# Initialize scores and checks
score = 0
len_ght = False
upp_er = False
low_erk = False
num_br = False
evryone_isspecial = False

# Checks the length
if len(password) >= 8:
    len_ght = True
    score += 1

# Check if there is an uppercase character
for char in password:
    if char.isupper():
        upp_er = True
        score += 1
        break

# Checks the lowercases
for char in password:
    if char.islower():
        low_erk = True
        score += 1
        break

# Checks if it includes numbers
for char in password:
    if char.isdigit():
        num_br = True
        score += 1
        break

# Check special characters
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
for char in password:
    if char in special_chars:
        evryone_isspecial = True
        score += 1
        break

# Print assessment
print()
print("Password strength assesment:")
print(f"Length of the password (8+ characters): {'Yes' if len_ght else 'No'}")
print(f"Contains  some uppercase letter: {'Yes' if upp_er else 'No'}")
print(f"Contains lowercase letters: {'Yes' if low_erk else 'No'}")
print(f"Contains any numbers: {'Yes' if num_br else 'No'}")
print(f"Contains any special characters: {'Yes' if evryone_isspecial else 'No'}")
print()
print(f"Strength score: {score}/5")

# Provide strength feedback
if score <= 2:
    strength = "Your password it's too weak make it stronger NOOOOWWW!!"
elif score == 3:
    strength = "MEh You can do it better...DO IT "
elif score == 4:
    strength = "YEI your password is strong GOOD JOB MY FELLA"
else:
    strength = "YOU ARE A MASTER IN PASSWORDS"

print(f"Password strength: {strength}")
