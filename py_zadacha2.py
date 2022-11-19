# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите значение х = '))
y = int(input('Введите значение y = '))
z = int(input('Введите значение z = '))
rezult1 = not(x or y or z)
rezult2 = not (x) and not(y) and not(z)
if rezult1 == rezult2:
   print("True")
else:
   print("False")