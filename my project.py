print("hello, this is my final project")
name = input ("what is your name? ")
print( "hi" + " " + name +", " + "nice to meet you" )
print("this is a special calculator, i would need two numbers from you")
number_1 = int(input("first number  : "))
number_2 = int(input("second number  : "))
print("thanks for puting in your numbers, " + str(number_1) +" "+ "and" + " " + str(number_2))
is_even=number_1 % 2 ==0  
is_even_number2=number_2 % 2==0

if is_even: #בודק האם המספר הראשון  זוגי
     number_is = "even"
else:#אחרת אי זוגי
    number_is = "odd"

print("i can see that the first number is "+ number_is)

if is_even_number2:#בודק האם המספר השני זוגי 
   status_number = "even"
else: #אחרת אי זוגי
    status_number ="odd"
print("and the second is " +status_number)

if is_even and is_even_number2: #בודק אם שני המספרים זוגיים אז מדפיס שניהם זוגיים
   print("so both are even")
elif not is_even and not is_even_number2:#בודק אם שני המספרים אי זוגיים אז מדפיס שניהם אי זוגיים
  print("so both are odd")
else: #אם אחד לא זוגי ואחד כן אז מדפיס אחד כן ואחד לא
    print("so one of them is " + number_is + ", and one is " + status_number )

import time #כדי שנוכל להשתמש בזמן בהמשך 

operator= input("+, - ,*, / :" )
devision = operator== "/"
plus = operator== "+"
minus= operator == "-"
result_plus= number_1 + number_2
result_minus= number_1 - number_2
result_multipication= number_1 * number_2

#עכשיו בודקים מה המשתמש בחר
if operator=="-":
    print(str(number_1) + " - " + str(number_2) +  " = " + str(result_minus ))
elif operator=="*": 
    print(str(number_1) + " * " + str(number_2) +  " = " + str(result_multipication))
elif operator== "+":
      print(str(number_1) + " + " + str(number_2) +  " = " + str(result_plus ))
elif operator=="/":
  print("you chose division should the result be integer? " )
else:
    print("error try again")

if not operator=="/":#אם לא חילוק שידפיס 
 print("thank you "+ name + " for using the calculate on "+str(time.ctime()))

if operator=="/" : #אם זה חילוק שיבדוק מה המשתמש  בחר
  answer= input("y/n ") 
  answer_is_y = answer =="y" 


if number_2==0 and operator=="/":       #אם התוצאה אפס וזה חילוק שיעצור את התוכנה
   print("error number_2 is zero")
   print("please try again ")
elif  operator=="/" and answer_is_y :   #אם המשתמש ענה כן  וזה חילוק
   result_devision_int= number_1 // number_2
   print(str(number_1) + " / " + str(number_2) +  " = " + str(result_devision_int))   # מספר שלם
elif operator=="/" and not answer_is_y: #אם המשתמש ענה לא וזה חילוק
   result_devision_float = number_1 /number_2
   print(str(number_1) + " / " + str(number_2) +  " = " + str(result_devision_float))    #מספר עם שארית
 
if operator=="/":# אם חילוק שידפיס
 print("thank you "+ name + " for using the calculate on "+str(time.ctime()))















