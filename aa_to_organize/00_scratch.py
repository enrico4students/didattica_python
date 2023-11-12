nome = "maria"

tmp = list(nome)    # to list, lists are mutable
tmp[-1] = "o"       # assign
nome = "".join(tmp) # back to string

print(nome)

s = "xxxxx"
i = 2
s = s[:i]+"y"+s[i+1:]
print(s)

asasa = [}