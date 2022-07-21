import math
list=[]
n = int(input('Nhap vao so nguyen duong n = '))
i=1
while i < n:
    x = int(input('Nhập giá trị trong danh sách:"))
    list.append(x)
    i=i+1
print("Danh sách vừa nhập là:",list)
    if n < 2:
        print("Đây không là số nguyên tố")
    tg = int(math.sqrt(n))
    for i in range(2, tg + 1):
        if (n % i) == 0:
            print("Đây không là số nguyên tố")
    print("Đây là số nguyên tố)
if n >= 2:
    print(2)
    for i in range(3, n + 1):
        if isPrimeNum(i):
            print(i)
        i = i + 2
