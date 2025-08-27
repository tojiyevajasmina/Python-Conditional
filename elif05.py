height = float(input("bo'yingiz:"))
weight = float(input("vazningiz:"))

bmi = weight / pow(height,2)

if bmi < 18.5:
    print("kam vazn")
elif bmi < 25:
    print("normal vazn")
elif bmi < 30:
    print("ortiqcha vazn")
else:
    print("semizlik")