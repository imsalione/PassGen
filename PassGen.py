import random
import pyperclip

# لیست کاراکترهای خاص
special_chars = ['@', '#', '$', '%', '^', '&', '*']

# لیست کاراکترهای عمومی (حروف و اعداد)
general_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I',
'J', 'K', 'L', 'M', 'N', '0', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W',
'X', 'Y', 'Z', '1', '2', '3', '4',
'5', '6', '7' , '8' , '9']

# دریافت نام اکانت و شناسه از کاربر
account_name = input("Enter the account name: ")
user_id = input("Enter your ID: ")
account_name.capitalize()

# تعداد کاراکترهای پسورد
password_length = 16

# انتخاب حداقل دو کاراکتر خاص
password = random.sample(special_chars, 2)

# انتخاب بقیه کاراکترها از کاراکترهای عمومی
remaining_length = password_length - len(password)
password += random.choices(general_chars + special_chars, k=remaining_length)

# مخلوط کردن کاراکترها به صورت تصادفی
random.shuffle(password)

# تبدیل لیست کاراکترها به یک رشته
password = ''.join(password)

# نمایش اطلاعات
print(f"{account_name} password")
print(f"id: {user_id}")
print(f"password: {password}")

# ذخیره کردن پسورد در حافظه (clipboard)
pyperclip.copy(password)
print("Password has been copied to clipboard. You can paste it now!")

# مسیر و نام فایل
file_path = r'C:\password.txt'

# ذخیره اطلاعات در فایل به صورت افزودن (append)
with open(file_path, 'a') as file:
    file.write(f"\n{account_name} password\n")
    file.write(f"id: {user_id}\n")
    file.write(f"password: {password}\n")

print(f"Password saved in {file_path}")