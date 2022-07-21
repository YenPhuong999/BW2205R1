##bài 1: Khai báo một danh sách chứ tên các môn học ở học kỳ này:
###a.Hãy dùng vòng lặp for in ra danh sách
monhoc=['Nền tảng máy tính','Cơ sở dữ liệu','Giao tiếp trong kinh doanh','Kỹ năng mềm','Bơi lội','Nguyên lý KT']
for i in range(len(monhoc)):
    print(monhoc[i])
###b.Dùng vòng lặp while in ra danh sách
k=0
while k < len(monhoc):
    print(monhoc[k])
    k=k+1
###c.Câp nhật danh sách tại vị trí thứ 2 là môn'Python cơ bản'
monhoc.insert(2,'Python cơ bản')
print(monhoc)
###d.Thêm môn'Python nâng cao' vào cuối danh sách
monhoc.insert(-1,'Python nâng cao')
print(monhoc)
###e.Thêm môn học 'Hướng đối tượng' vào đầu danh sách
monhoc.insert(1,'Hướng đối tượng')
print(monhoc)
###f.Kiểm tra xong trong danh sách có môn học'Pythin cơ bản' không ?
x='Python cơ bản'
if x in monhoc:
    print('Có',x,'trong danh sách môn học')
else:
    print('Không có',x,'trong danh sách môn học')
###g.Xóa trong danh sách môn học'Hướng đối tượng'
monhoc.remove('Hướng đối tượng')
print(monhoc)
###h.Làm rỗng danh sách đã cho
monhoc[ ]
print(monhoc)


