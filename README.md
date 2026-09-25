USTH Advanced Programming with Python 2026
==================================

* Dinh Hoang Long
* 2410555

import math 
def program1():
   r=float(input("Enter circle radius:"))
   area = math.pi *r**2
   print("Circle area:", area)


def program2():
   x=float(input("Enter the temperature in Celsius?"))
   F=(x*9/5)+32
   print(x, "(C) =",F,"(F)")

def program3():
   x=int(input("Enter a number:"))
   prime = True
   if x<=1:
     prime = False
   else:
     for i in range(2,x):
        if x%i==0:
            prime = False
            break
   if prime:
      print(x,"is a prime number")
   else:
      print(x,"is NOT a prime number")

def program4():
   x=int(input("Enter a number:"))
   sum =0
   for i in range(1,x):
      if x%i==0:
        sum =sum+i
   if sum==x:
      print(x,"is a perfect number")
   else:
      print(x,"is not a perfect number")

def program5():
   colors=["Blue","Yello","Black","Red"]
   color=input("What's your favourite color?")
  if color in colors:
      print("Your color is at index", colors.index(color),"in my list")
  else:
      print("Sorry I couldn't find your color")

def program6():
    a=range(0,7)
    print(list(a))
    b=range(1,11,3)
    print(list(b))
    c=range(5,0,-1)
    print(list(c))
    d=range(6,-2,-2)
    print(list(d))

 def program7():
     def remove_dollar_sign(s):
        return s.replace("$","")
    print(remove_dollar_sign("$100"))

 def program8():
     def extract_even(l):
        result=[]
        for x in l:
            if x%2 ==0:
                result.append(x)
        return result
    print(extract_even([1,4,5,-1,10]))

 def program9():
      def factorial(n):
          result=1
          for i in range(1,n+1):
              result=result*i
          return result

def program10():
    def get_divisors(n):
        result=[]
        for i in range(1,n+1):
            if n%i==0:
                result.append(i)
            return result

def program11():
    def compute_distance_between_points(p1,p2):
        x1,y1=p1
        x2,y2=p2
        distance=((x2-x1)**2+(y2-y1)**2)**0.5
        return distance
def program12():
    def print_pattern(m,n):
      for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    print_pattern(4,5)

    
