dinhmuc = 100
listgia=[4500,5500,8500,10000,20000]
chisocu = int(input("Hãy nhập vào chỉ số cũ:"))
chisomoi = int(input("Hãy nhập vào chỉ số mới:"))

luongdiensd = chisomoi - chisocu
print("Lượng điện sử dụng trong tháng :",luongdiensd)

if luongdiensd > dinhmuc:
    vuotdm = luongdiensd - dinhmuc
else :
    vuotdm = 0
    luongdiensd = dinhmuc
print ("Vượt định sd:", vuotdm)

if vuotdm < 100:
    x2 = (luongdiensd * listgia[0])/dinhmuc
    print("Tổng tiền điện =",x2)
else:
    x1 = listgia[0] * dinhmuc
    print("Số tiền điện nằm trong định mức =",x1)
    if vuotdm == 100:
        x2 =  listgia[0]*dinhmuc * vuotdm
        print ("Số tiền điện vượt định mức =",x2)
    elif 100 < vuotdm <= 200 :
        x2 = listgia[1] * vuotdm
        print("Số tiền điện vượt định mức =",x2)
    elif 200 < vuotdm <= 500:
        x2 = listgia[2] * vuotdm
        print("Số tiền điện vượt định mức =",x2)
    elif 500 < vuotdm <=800 :
        x2 = listgia[3] * vuotdm
        print("Số tiền điện vượt định mức =",x2)
    else :
        tienvuotdm = listgia[4] * vuotdm
        print("Số tiền điện vượt định mức =",x2)
    S = x1 + x2
    print("Tổng tiền điện trong 1 tháng của gia đình là :",S)

    


    
    


