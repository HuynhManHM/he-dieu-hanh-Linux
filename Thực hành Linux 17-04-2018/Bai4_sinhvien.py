class sinhvien:
	def __init__(self,mssv,hoten,khoa):
		self.mssv=mssv
		self.hoten=hoten
		self.khoa=khoa
	def setmssv(self,mssv):
		self.mssv=mssv
	def setten(self,hoten):
		self.hoten=hoten
	def setkhoa(self,khoa):
		self.khoa=khoa
	def getmssv(self):
		return self.mssv
	def getten(self):
		return self.hoten
	def getkhoa(self):
		return self.khoa
	def toString(self):
		print self.mssv," - ",self.hoten," - ",self.khoa
		
	
		 
