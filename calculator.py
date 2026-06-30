
running = True 
while running:
    cal = input("what would u like to do?" \
"add,sub,per,dvd,mul:")
    if (cal == "add"):
        a = int(input("enter the first number "))
        b = int(input("enter the second number "))
        sum = a + b
        print(sum)
    elif (cal == "sub"):
          a = int(input("enter the first number "))
          b = int(input("enter the second number"))
          sub = a - b
          print(sub)
    elif (cal == "per"):
          a = int(input("enter the first number "))
          b = int(input("enter the second(out of) number"))
          per = (a / b )*100
          print(per)
    elif (cal == "dvd"):
         a = int(input("enter the first number "))
         b = int(input("enter the second number"))
         if (b == 0):
              print("you cant divide 0")
         else:
          dvd = a / b
          print(dvd)
    elif (cal == "mul"):
          a = int(input("enter the first number "))
          b = int(input("enter the second number"))
          mul = a*b
          print(mul)
    else:
         print("invalid ")
    run = input("would you like to calculate again?,yes or no")
    if (run== "no"):
         running = False 
         print("thanks for using calculator!")


 







