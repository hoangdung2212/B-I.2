print("Sinh vien: Hoang Van Dung")
print("MSSV:235752021610063")
a, b =1, 2
total = 0
print(a,end=" ")
while (a <=4000000-1):
    if a % 2 == 0:
        total+=a
    a, b =b, a+b
    print (a,end=" ")

print("\n Tong cac co da in trong day la: ",total)
