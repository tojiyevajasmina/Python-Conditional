name_file = "python"

file = input("fayl nomini kiriting:")

if name_file in file and len(name_file) == 6:
    print(f"{file} nomli fayl mavjud")
else:
    print(f"{file} nomli fayl topilmadi ")