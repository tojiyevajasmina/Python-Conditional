km = int(input("masofani kiriting:"))

if 0 <= km  <= 1 :
     print("Piyoda yuring")
elif 1  <= km  <= 5 :
     print("Velosiped yoki elektr skuter")
elif 5  <=  km  <= 50 : 
     print("Avtobus yoki mashina")
elif 50 <= km :
     print("Poyezd yoki samolyot")
else:
     print("Masofa manfiy bo'la olmaydi!")