# Comandos condicionais.

# Se
if 5 > 2: # True
    print("executado")
    
print("tanto faz")

# Senão
if 2 > 5: # False
    print('nao foi executado')
else:
    print('excutado')
    
# Senão se, (estrutura condicional aninhada)

if 2 > 3: # False
    print('nao foi executado')
elif 5 > 2: # True
    print('executado')
else:
    print('nao teve jeito')
