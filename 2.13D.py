print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
import math
a = int(input ("Nhập hệ số a: "))
b = int(input ("Nhập hệ số b: "))
c = int(input ("Nhập hệ số c: "))

delta = b^2 - 4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print ("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print (f"Nghiệm của phương trình là: x = {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print (f"Có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print (f"Có một nghiệm kép: x = (x)")
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-delta) / (2*a)
        print(f"Có hai nghiệm phức: x1 = (real_part) + (imaginary_part)i,")

