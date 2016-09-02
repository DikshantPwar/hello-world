class addition:
      sum=0
      def __init__(self,a,b):
         self.a=a
         self.b=b
         addition.sum=a+b
      def displayaddition(self):
         print("sum",addition.sum)
x=addition(1,2)
x.displayaddition()
print("total sum is:%d" % addition.sum)
class multiplication:
      def __init__(self,a,b):
            multiplication.mult=a*b
      def displaymultiplication(self):
            print("mult is:%d" % multiplication.mult)
y=multiplication(1,2)
y.displaymultiplication()

