a=input("Nhap a: ")
b=input("Nhap b: ")
def tong(a,b):
	return a+b
def tru(a,b):
	return a-b
def nhan(a,b):
	return a*b
def tong(a,b):
	return a+b
def chia(a,b):
	return a/b
def laydu(a,b):
	return a%b
def luythua(a,b):
	kq=1
	for i in(0,b,1):
		kq*=a
	return kq
print"Tong 2 so la: ",tong(a,b)
print"Hieu 2 so la: ",tru(a,b)
print"Tich 2 so la: ",nhan(a,b)
print"Thuong 2 so la: ",chia(a,b)
print"Chia lay du 2 so la: ",laydu(a,b)
print"Luy thua so a la: ",luythua(a,b)

