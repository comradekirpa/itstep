slovo = str(input("Тест палиндром - введите слово"))
x = len(slovo)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if slovo[x - i] == slovo[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")