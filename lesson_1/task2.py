# задание 2
n=int(input("укажите число"))
hour=(int(n)//3600)
print({hour})
minuta=((int(n)%3600)//60)
print({minuta})
sec=((int(n)%3600)%60)
print({sec})
print(f"{hour:02d}:{minuta:02d}:{sec:02d}")