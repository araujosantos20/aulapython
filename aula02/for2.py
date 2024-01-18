#variável de contagem

k = 0
for i in range(1,201): 
    if i %2 == 0 :
        k = k + 1


print("A quantidade de números pares entre 1 e 200 é:")
print(k) 