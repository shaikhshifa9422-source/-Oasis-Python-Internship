# Oasis Infobyte - Task 2 - Random Password Generator
# ID: OIB/O2/IP3914 - Shifa Shaikh

import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

password = "".join(random.choice(all_chars) for i in range(length))
print(f"Generated Password: {password}")