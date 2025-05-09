# n= range(1,11)
# quadrado={x**2 for x in n}
# print(quadrado)
###########################################################################################
# palavras = ["python", "java", "c++", "javascript"]
# capittalizadas={x.capitalize() for x in palavras}
# print(capittalizadas)
###########################################################################################
# frase= "Eu adoro programação em Python"

# lista={x for x in frase if x.lower() not in 'aeiouã'}
# print("".join(lista))
###########################################################################################
# numero= range(1,101)

# quadrado_perfeito={x for x in numero if (x ** 0.5).is_integer()}
# print(quadrado_perfeito)
###########################################################################################
# frutas = ["maçã", "banana", "uva", "laranja", "kiwi", "melancia"]

# mais= {x for x in frutas if len(x)>=4 }
# print(mais)
############################################################################################
# frases = ["olá mundo", "python é divertido", "compreensão de lista"]

# invertida={x[::-1] for x in frases}
# print(invertida)

# nomes = ["Ana Clara", "Bruno Silva", "Carla Souza", "Daniel Pereira"]
# primeira=sorted({x[0] for x in nomes})
# print(primeira)

############################################################################################

# b = range(1, 11)

# dic = {
#     x: x ** 3 for x in b 
# }

# for x in dic.items():
#     print(x)
############################################################################################


# frase= "Python é incrível"

# contagem={}

# for i in frase:
#     contagem[i] = contagem.get(i, 0) + 1

# print(contagem)
##############################################################################################
# b = range(1, 21)
# dic={
#     x:"par" if x % 2 == 0 else "ímpar" for x in b 
# }
# print(dic)
#############################################################################################