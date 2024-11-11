

def q1(): 
  #Write Assignment code here
  word= input("In: ")
  word= str(word)
  if word[-1:] == "y":
     print("-ies")
  elif word[-2:] == "ey":
     print("-eys")
  elif word[-3:] == "ife":
     print("-ives")
  else:
     print("-s")


def q2(): 
  #Write Assignment code here
  num= input("In: ")
  num= int(num)
  if num > 0:
      print(f"{num} is positive")
  elif num < 0:
      print(f"{num} is negative")


def q3():
   num1= input("In: ")
   num2= input("In: ")
   num3= input("In: ")
   num1 = float(num1)
   num2 = float(num2)
   num3 = float(num3)
   if num1 == num2 == num3:
      print("Equilateral")
   elif num1 == num2 and num1 != num3:
      print("Isosceles")
   elif num2 == num3 and num2 != num1:
      print("Isosceles")
   elif num1 == num3 and num1 != num2:
      print("Isosceles")
   elif num1 != num2 and num2 != num3:
      print("Scalene")
   elif num1 + num2 != num3:
      print("No Triangle")
   elif num2 + num3 != num1:
      print("No Triangle")
   elif num1 + num3 != num2:
      print("No Triangle")




#Do not alter the following code
#Comment out the following code when running your tests
#q1()
#q2()
#q3()
