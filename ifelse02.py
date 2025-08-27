password = input("tekshirish uchun parol kiriting:")

if len(password) > 8 and "A" < password < "Z" :
    print("parol qabul qilindi")
else:
    print("parol noto'g'ri. Kamida 8 ta belgi 1 harf va 1 raqam bo'lishi kerak.")