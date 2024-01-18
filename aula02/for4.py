import os

k = 0
os.system("clear")
for i in range(1973, 2023): 
    if i %4 == 0 :
        k = k + 1


print("A quantidade de anos que foram bissextos entre os anos de 1973 e 2023 é")
print(k) 