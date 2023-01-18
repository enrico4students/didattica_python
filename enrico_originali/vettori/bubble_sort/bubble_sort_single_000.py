vettore = [9, 1, 8, 2, 7, 3, 6, 4, 5]

for i in range(len(vettore)):
    for j in range(i+1,len(vettore)):
        if vettore[i]>vettore[j]:
            vettore[i], vettore[j] = vettore[j], vettore[i]

print(vettore)
