
class veriler():
    def __init__(self,iş , maaş , dilleri):
        self.iş = iş
        self.maaş = maaş
        self.dilleri = dilleri

    def bilgilerigöster(self):
     print("""isim : {}
,maaş : {} 
,dilleri : {} 
      """.format(self.iş,self.maaş,self.dilleri))

    def dilekleme(self,yenidil):
        print("dil eklendi")
        self.dilleri.append(yenidil)

    def zam(self,yenimaaş):
        print("zam yapıldı")
        self.maaş+=yenimaaş

yazılımcı = veriler("veritabanı uzmanı" , 5000 , "Python")

print(yazılımcı.zam(100))
print(yazılımcı.bilgilerigöster())