# ДЗ урок 2 "Условная конструкция. Операторы if, elif, else." module_2_2.py
first = 132
second = 358
third = 796
a = ([first % 10,  second // 100, second % 10, third % 10,  first % 10, second // 100])
print(a)
print(a[:2])
mid = a[2:4]
print(mid)
print('2'+'3')
print('8'+'6')
print('2'+'3')
first1 = 23
second1 = 86
third1 = 23

if first1 == third1 == second1 and second1 != first1 != third1:
    print(3)
elif first1 == third1:
    print(2)
if first1 != third1 and second1 != first1 and second1 != third1:
    print(0)
else:
    print(False)



