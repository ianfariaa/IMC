peso =int( input("Digite o seu peso (KG): "))
altura = float(input('Digite sua altura?(M):'))
idade = int(input('Digite sua idade: '))
Imc = peso / (altura ** 2)
print("Seu IMC é {:.1f}".format(Imc))
if Imc < 18.5:
    print("Você está ABAIXO do PESO NORMAL")
elif 18.5 <= Imc < 25.0:
    print('PARABENS ! Você está no PESO IDEAL!')
elif 25.0 <= Imc < 30:
    print('Você está SOBREPESO.')
elif 30 <= Imc < 40:
    print('Você está em OBESIDADE')
elif Imc >= 40:
    print('Você está em OBESIDADE MORBIDA, PERCA PESO IMEDIATAMENTE!!!')



# O fator idade eu preciso refazer, e encaixar nisso.