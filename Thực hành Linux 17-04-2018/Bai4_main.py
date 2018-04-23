from sinhvien import sinhvien
from khoa import khoa
l=[]
sv=sinhvien("001","Huynh Man","57")
l.append(sv)
sv=sinhvien("002","Huynh A","56")
l.append(sv)
sv=sinhvien("003","Huynh B","58")
l.append(sv)
sv=sinhvien("004","Huynh C","59")
l.append(sv)
sv=sinhvien("005","Huynh D","57")
l.append(sv)
sv=sinhvien("006","Huynh E","57")
l.append(sv)
size =len(l)
i=0
while i<size:
	l[i].toString()
	i=i+1
listkhoa=[]
kh=khoa("56","khoa 56 CNTT")
listkhoa.append(kh)
kh=khoa("57","khoa 57 CNTT")
listkhoa.append(kh)
kh=khoa("58","khoa 58 CNTT")
listkhoa.append(kh)
kh=khoa("59","khoa 59 CNTT")
listkhoa.append(kh)
size =len(listkhoa)
a=0
while a<size:
	listkhoa[a].toString()
	a=a+1
b=0
while b<len(l):
	if(l[b].getkhoa()=="57"):
		l[b].toString()
	b=b+1
