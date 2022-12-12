# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = range(2)
y = range(2)
z = range(2)
if (not(x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False)
    

