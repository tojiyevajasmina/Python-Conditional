email = input("emailingizni kiriting:")

if "@" in email and (email[-4:] == ".com" or email[-3:] == ".uz" or email[-4:] == ".net" or email[-4:] == ".org"):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")