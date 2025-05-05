import time
import os 
os.system('cls')

frase= "Banco do Python"

f=frase.center(30,'-')

print(f)
print('O que você deseja fazer?')
print('1-saldo\t                        2-saque')
print('3-deposito\t                4-transferência')


e=int(input())

os.system('cls')

print('Carregando', end="")

for i in range(3):
    time.sleep(1)
    print('.',end='', flush=True )

os.system('cls')

def c_saldo():
     try:
      with open("saldo.txt","r") as arquivo:
        conteudo = arquivo.read().strip()
        if conteudo:
         valor = float(conteudo)
        else:
           valor= 0.0
     except FileNotFoundError:
      return 0.0
     except ValueError:
      valor = 0.0
     return valor

def saque():
    try:
        with open("saldo.txt", "r") as arquivo: 
            conteudo = arquivo.read().strip()  
            if not conteudo:  
                valor = 0.0  
            else:
                valor = float(conteudo)
                
            if valor > 0.0:
                print(f"Saldo disponível: R${valor:.2f}")
                r = int(input('Deseja sacar? (1-sim  2-não): '))
                if r == 1:
                    n = float(input("Quanto deseja sacar? "))
                    if n > valor:
                        print("Você está tentando sacar mais do que tem.")
                    else:
                        valor = valor - n
                        with open("saldo.txt", "w") as arquivo:
                            arquivo.write(str(valor))
                        print(f"Saque realizado! Agora você possui: R${valor:.2f}")
                else:
                    print('Ok, tenha um bom dia!')
            else:
                print("Você não possui saldo suficiente para realizar o saque.")
    except FileNotFoundError:
        print("Arquivo de saldo não encontrado.")

def deposito():
   n = float(input('Digite o valor que deseja depositar: '))
   
   if n > 0:
      try:
          with open("saldo.txt", "r") as arquivo:
              conteudo = arquivo.read().strip() 
              if not conteudo:  
                  valor = 0.0  
              else:
                  valor = float(conteudo)  
          valor = valor + n 

          with open("saldo.txt", "w") as arquivo:
              arquivo.write(str(valor))  
              
          print(f"Seu saldo agora é de R${valor:.2f}")
          
      except FileNotFoundError:  
          with open("saldo.txt", "w") as arquivo:
              arquivo.write(str(n))  
          print(f"Seu saldo agora é de R${n:.2f}")
   
   elif n < 0:
      while n < 0:
          print("Você quer depositar um valor negativo?")
          time.sleep(2)
          n = float(input('Digite o valor.'))  

   elif n == 0:
      while n == 0:
          print("Você quer depositar 0 reais?")
          time.sleep(2)
          n = float(input('Digite o valor.'))  

      
def transferencia():
    with open("saldo.txt","r") as arquivo:
     valor=float(arquivo.read())

    print(f'Você tem R${valor} reais')
    val(valor)
def val(valor):
     while True:
        t = float(input('Quanto você deseja transferir? '))
        if t > valor:
            print("Você está tentando transferir mais do que tem.")
            continue
        break
     print('Para quem?')
     while True: 
      p=input('Digite o número da conta(5 digitos): ')
      if len(p)==5 and p.isdigit() :
        break
      print("Número incorreto(apenas 5 números por favor)")
        
     print(f'R${t} para a conta {p}, confirma?(1-sim e 2-não)')
     d=int(input())
     if d==1:
       valor=valor-t
       print('Valor tranferido.')
       with open("saldo.txt", "w") as arquivo:
          arquivo.write(str(valor))
          print(f"Seu saldo é de R${valor} reais")
     elif d==2:
        print('Qual o problema?')
        print('1-desistência.')
        print('2-Errei o número da conta ou o valor.')
      
     o=int(input())
     if o==1:
        print("Ok,até a próxima")
     elif o==2:
       val(valor)
      

while True:
  
  if e==1:
    saldo=c_saldo()
    print(f'Você tem R${saldo} reais')
    
    break

  if e==2:
    saque()
    break
    
  if e==3:
    deposito()
    break

  if e==4:
    transferencia()
    break

  else:
   print("operação inválida")
   print('O que você deseja fazer?')
   print('1-saldo\t                        2-saque')
   print('3-deposito\t                4-tranferência')
   try:
            e = int(input())
   except ValueError:
            e = 0


      

   
   



      

