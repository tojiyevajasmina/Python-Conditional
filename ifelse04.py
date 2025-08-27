balans = 5000
summani_yechish = int(input("qancha oul yechmoqchisz?"))

if summani_yechish < 0:
    print("Manfiy summa kiritib bo'lmaydi.")
elif summani_yechish <= balans:
    balans -= summani_yechish
    print(f"Pul yechildi. Qolgan balans: {balans} so'm")
else:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")
