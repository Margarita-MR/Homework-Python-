# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Вариант 1

print('Введите номер дня недели - ',end='') 
day=int(input())
# norm_wd = [1,5]
# norm_sd = [6,7]
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5: 
    print(f'{day} -> нет')

elif day == 6 or day == 7: 
    print(f'{day} -> да')
else:
    print('В неделе 7 дней!!!')


#  Вариант 2

# print('Введите номер дня недели - ',end='') 
# day=int(input())
# if day==1:
#     print('нет')
# elif day==2:
#     print('нет')
# elif day==3:
#     print('нет')
# elif day==4:
#     print('нет')
# elif day==5:
#     print('нет')
# elif day==6:
#     print('да')
# elif day==7:
#     print('да')
# else: 
#     print('в неделе 7 дней')