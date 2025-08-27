# chipta narxi
narx = 100

#foydalanuvchidan yoshni kiritish suraladi
yosh = int(input("yoshingizni kiriting:"))

if yosh <= 6:
    print(narx *0.5)
if yosh <= 17:
    print(narx *0.8 )
if yosh >= 60:
    print(narx *0.7)
else:
    print(f"yakuniy narx:{narx}so'm")


