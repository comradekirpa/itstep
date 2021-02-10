a = int(input("Введи число"))

if a%3==0 and a%5==0:
     print("FuzzBuzz")
elif a%3==0:
    print("Buzz")
elif a%5==0:
    print("Fuzz")
if a > 100:
    print("Error")

