# задание 6
a=int(input("кол-во пройденных км в первый день>>>"))
b=int(input("Желаемый результат>>>"))
counter=1
while a<b:
    a=a*1.1
    counter=counter+1
else:
    print(f"Done! Вам потребовалось {counter} дней")
