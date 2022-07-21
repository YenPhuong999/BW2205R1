n = int(input("Nhập vào chiều cao n =:"))
for i in range (n):
    for j in range (n):
        if i==j or i + j == n-1        :
            print("*", end = ' ')
        else:
           print(" ", end=' ')
    print()
