# ДЗ урок 2 "Условная конструкция. Операторы if, elif, else." module_2_2.py
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
