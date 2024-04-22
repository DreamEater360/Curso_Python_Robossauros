# # Manipulação de Strings

# # Concatenação
# a = "Hello"
# b = "World"
# concatenacao = a + ", " + b
# print(concatenacao) 

# # Substring
# s = "Python"
# print(s[0])     # Saída: P
# print(s[1:4])   # Saída: yth
# print(s[-1])    # Saída: n

# # Formatação

# nome = "Maria"
# idade = 30
# print("Nome: {}, Idade: {}".format(nome, idade))
# # Saída: Nome: Maria, Idade: 30

# print(f"Nome: {nome}, Idade: {idade}")
# # Saída: Nome: Maria, Idade: 30

# # Formatação de case

# s = "python é divertido"
# print(s.upper())        # Saída: PYTHON É DIVERTIDO
# print(s.lower())        # Saída: python é divertido
# print(s.capitalize())   # Saída: Python é divertido
# print(s.title())        # Saída: Python É Divertido

# # Pesquisa e substituição 

# s = "python é uma linguagem de programação, e Python é divertido"
# print(s.find("Python"))          # Saída: 41
# print(s.replace("Python", "C"))  # Saída: python é uma linguagem de programação, e C é divertido
# print(s.count("Python"))         # Saída: 2

# # Metodos importantes

# s = "Python"
# print(len(s))  # Saída: 6

# s = "   Python   "
# print(s.strip())   # Saída: "Python"
# print(s.rstrip())   # Saída: "   Python"
# print(s.lstrip())   # Saída: "Python   "

# s = "Python é uma linguagem de programação"
# palavras = s.split(" ")
# print(palavras)   # Saída: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

# palavras = ['Python', 'é', 'divertido']
# s = " ".join(palavras)
# print(s)   # Saída: "Python é divertido"

# s = "Python é uma linguagem de programação"
# print(s.index("linguagem"))   # Saída: 13

# s = "Python é divertido"
# print(s.startswith("Python"))   # Saída: True
# print(s.endswith("divertido"))  # Saída: True
