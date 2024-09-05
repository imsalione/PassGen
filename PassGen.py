import random
import pyperclip

# List of special characters
special_chars = ['@', '#', '$', '%', '^', '&', '*']

# List of general characters (letters and digits)
general_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I',
'J', 'K', 'L', 'M', 'N', '0', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W',
'X', 'Y', 'Z', '1', '2', '3', '4',
'5', '6', '7', '8', '9']

# Get account name and user ID from the user
account_name = input("Enter the account name: ")
user_id = input("Enter your ID: ")

# Length of the password
password_length = 16

# Select at least two special characters
password = random.sample(special_chars, 2)

# Select the remaining characters from the general characters
remaining_length = password_length - len(password)
password += random.choices(general_chars + special_chars, k=remaining_length)

# Shuffle the characters randomly
random.shuffle(password)

# Convert the list of characters into a string
password = ''.join(password)

# Display the information
print(f"{account_name} password")
print(f"id: {user_id}")
print(f"password: {password}")

# Copy the password to the clipboard
pyperclip.copy(password)
print("Password has been copied to clipboard. You can paste it now!")

# File path and name
file_path = r'C:\password.txt'

# Save the information in the file (append mode)
with open(file_path, 'a') as file:
    file.write(f"\n{account_name} password\n")
    file.write(f"id: {user_id}\n")
    file.write(f"password: {password}\n")

print(f"Password saved in {file_path}")
