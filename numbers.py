class number:
  def __init__(self,n1,n2):
    self.product = n1*n2
    self.sub = n1-n2
    self.div=n1/n2
    self.add=n1+n2
n1=int(input("enter the number,n1 : "))
n2=int(input("enter the number,n2 : "))
p1 =number(n1, n2)

print("the product of two number is :",p1.product)
print("the difference of two number is:",p1.sub)
print("the addition of two number is:",p1.add)
print("the division of the two number is :",p1.div)