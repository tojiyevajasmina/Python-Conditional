#foydalanuvchidan harorat suraladi
harorat = int(input("haroratni kiriting:"))

if harorat < 0:
    print("juda sovuq!issiq kiyim kiying.")
if harorat >= 0 and harorat <= 14:
    print("Sovuq. Kurtka kiying.")
if harorat >= 15:
    print("Ob-havo yaxshi.")