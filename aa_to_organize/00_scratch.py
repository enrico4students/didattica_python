
l = [str(x) for x in range(10)]
print(', '.join(l))


####################
map_me_again = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = map(lambda l: [ l[1], l[0], l[2]], map_me_again)
print(result)
print(*result) # unpack



lista_interna = [1]
lista_esterna =  ["a", lista_interna]

lista_copiata = lista_esterna[::]
lista_copiata[1][0] = 99
print(lista_interna)



nome = "maria"

tmp = list(nome)    # to list, lists are mutable
tmp[-1] = "o"       # assign
nome = "".join(tmp) # back to string

print(nome)

s = "xxxxx"
i = 2
s = s[:i]+"y"+s[i+1:]
print(s)

