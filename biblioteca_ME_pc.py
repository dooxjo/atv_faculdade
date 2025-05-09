#biblioteca de verificação de senha
import string 
import os

def valida(senha):

  
       
    erro=[]
    tamanho= len(senha)
    if not any(i.isupper() for i in senha):
        erro.append('A senha deve conter pelo menos 1 letra maiúscula')
    
    if not any(i.isdigit() for i in senha):
        erro.append('A senha deve conter pelo menos 1 número')
    
    caracteres_especiais = string.punctuation
    if not any(i in caracteres_especiais for i in senha):
        erro.append('A senha deve conter pelo menos 1 caracter especial')
    if tamanho<8:
        erro.append('A senha tem que ter no mínimo 8 caracteres')
    
    if erro:
        return '\n'.join(erro)

    else:
        return 'senha correta'
      



def pedir():
    while True:
        
        senha = input('Digite a senha: ')
        resultado = valida(senha)
        if resultado == 'senha correta':
            os.system('cls')
            print('Senha correta!')
            break
        else:
            print(resultado)

    
