password = input("Enter password: ")

digit = False

for ch in password:
    if ch.isdigit():
          digit = True

if len(password) >= 8 and digit:
    print("Strong password")
else:
    print("Weak password")

