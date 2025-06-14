'''
Exercícios sobre os comandos de condição em python
'''
from datetime import date, datetime
from deep_translator import GoogleTranslator

HOJE = datetime.now()
tradutor = GoogleTranslator (source= "en", target = "pt")

def exemploSe():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    else:
        if media >= 3:
            print('RECUPERAÇÃO')
        else:
            print('REPROVADO')

def exemploSe_elif():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    elif media >= 3:
        print('RECUPERAÇÃO')
    else:
        print('REPROVADO')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    soma = num1 + num2
    if soma > 10:
        print(f'{soma} é maior que 10')
    else:
        print(f'{soma} não é maior que 10')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

def q2():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    soma_dos_valores = (valor1 + valor2)
    if (soma_dos_valores > 20):
        print (soma_dos_valores + 8)
    if (soma_dos_valores <= 20):
        print (soma_dos_valores - 5)


#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num1 = int(input("Digite um número: "))
    resultado = (num1%3)

    if (resultado == 0 ):
        print ("É múltiplo de 3")
    else:
        print ("Não é múltiplo de 3")


#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.

def q4():
    num = int(input("Digite um número: "))
    resultado = (num%5)

    if (resultado == 0 ):
        print ("Esse número é divisível por 5 ")
    else:
        print ("Esse número não é divisível por 5 ")

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

def q5():
    num = float(input("Digite um número: "))

    if (num%3 == 0 and num%7 == 0 ):
        print ("Esse número é divisível por 3 e 7 ")
    else:
        print ("Esse número não é divisível por 3 e 7 ")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

def q6():
    salario = float(input("Digite o seu salário: "))
    valor_prestacao = salario * 0.30

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
    data_str = input("Data de Nascimento (dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")

    if (data_nascimento > HOJE):
        print ("Data inválida! Você nem nasceu ainda kkk.")
    else:
       print (f"Idade: {int((HOJE - data_nascimento). days/365)} anos.")


#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

def q10():
    a = int(input("Digite o primeiro inteiro: "))
    b = int(input("Digite o segundo inteiro: "))
    c = int(input("Digite o terceiro inteiro: "))

    if (a < b < c): #Equivale a if (a < b < c < )
     print(f"{a} {b} {c}")
    if (a < c < b):
        print (f" {a} {c} {b}")
    if (b < a < c):
        print (f" {b} {a} {c}")
    if (b < c < a):
        print (f" {b} {c} {a}")
    if (c < a < b):
        print (f" {c} {a} {b}")
    if (c < b < a):
        print (f" {c} {b} {a}")               

#11. Faça um programa que leia 3 números e imprima o maior deles.

def q11():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    if (num1>num2>num3):
        print("O primeiro número é o maior")
    if (num1>num3>num2):
        print("O primeiro número é o maior")
    if (num2>num1>num3):
        print("O segundo número é o maior")
    if (num2>num3>num1):
        print("O segundo número é o maior")
    if (num3>num1>num2):
        print("O terceiro número é o maior")
    if (num3>num2>num1):
        print("O terceiro número é o maior")

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

def q12():
    idade = int(input("Digite a sua idade: "))
    if (idade >= 18):
        print("Você é maior de idade")
    if (idade < 18):
        print("Você é menor de idade")
    if (idade > 65):
        print("Você é idoso")

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():

    nome = ("Digite o seu nome: ")
    prova1 = int(input("Digite a nota da prova: "))
    prova2 = int(input("Digite a nota da prova: "))
    media_prova = prova1

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    salario = float(input("Digite o seu salário: "))
    desconto_inss = 

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

def q18():
    mes = int(input('Número do Mês: '))
    if mes < 1 or mes > 12:
        print('Mês Inválido!')
    else:
        data = datetime.strptime(f'01/{mes}/25', '%d/%m/%y')
        mes_extenso = data.strftime('%B')
        print(tradutor.translate ("Month:" + mes_extenso))



#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
    menu_prato_entrada = '''
    [1] - Vegetariano (180 kcal)
    [2] - Peixe (230 kcal)
    [3] - Frango (250 kcal)
    [4] - Carne (350 kcal)
    Digite a opção de entrada [1-4]
    '''

    menu_bebida = '''
    [1] - Chá (20 kcal)
    [2] - Suco de Laranja (70 kcal)
    [3] - Suco de Melão (100 kcal)
    [4] - Refrigerante Diet (65 kcal)
    Digite a opção de entrada [1-4]
    '''

    menu_sobremesa = '''
    [1] - Abacaxi (75 kcal)
    [2] - Sorvete Diet (110 kcal)
    [3] - Mousse Diet (170 kcal)
    [4] - Mousse de Chocolate (200 kcal)
    Digite a opção de entrada [1-4]
    '''

    prato_entrada = int(input(menu_prato_entrada))
    bebida = int(input(menu_bebida))
    sobremesa = int(input(menu_sobremesa))

    cal = 0

    cal += 180 if prato_entrada == 1 else 0;
    cal += 230 if prato_entrada == 2 else 0;
    cal += 250 if prato_entrada == 3 else 0;
    cal += 350 if prato_entrada == 4 else 0;
    cal += 20 if bebida == 1 else 0;
    cal += 70 if bebida == 2 else 0;
    cal += 100 if bebida == 3 else 0;
    cal += 75 if bebida == 4 else 0;
    cal += 75 if sobremesa == 1 else 0;
    cal += 110 if sobremesa == 2 else 0;
    cal += 170 if sobremesa == 3 else 0;
    cal += 200 if sobremesa == 4 else 0;

    print(f"Total de calorias do pedido: {cal} kcal")

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

questao = int(input("Questão a executar: "))
eval(f"q{questao}()")