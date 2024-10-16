

def q1(): 
  #Write Assignment code here
  word= input("Input a word: ")
  if word[0:-1] == "y":
     print("-ies")
  elif word[0:-2] == "ey":
     print("-eys")
  elif word[0:-3] == "ife":
     print("-ives")
  else:
     print("-s")


def q2(): 
  #Write Assignment code here
  num= input("Input an integer: ")
  num= int(num)
  if num > 0:
      print(f"{num} is positive")
  elif num < 0:
      print(f"{num} is negative")



#Do not alter the following code
#Comment out the following code when running your tests
q1()
q2()
