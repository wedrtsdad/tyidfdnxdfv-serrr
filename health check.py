class d():
    def __init__(self):
        print("I'm a Doctor")
        
    def B(w,h):
        bmi= w/(h*h)
        print(str(bmi))
        
    def hr(fhr):
        if(fhr > 60 and fhr < 100):
            print("Your heart rate is normal")
        else:
            print("Your heart rate is not normal")
            
class p(d):
    def __init__(self,n,w,h,fhr):
        self.w=w
        self.h=h
        self.fhr=fhr
        self.n=n
        
    def c(self):
        print("\n name:"+ self.n)
        d.B(self.w,self.h)
        d.hr(self.fhr)
        
p1= p("Mr.Whatever",32,7.0,90)
p1.c()
  
p2= p("Mrs.Whatever",40,5.0,50)
p2.c()  