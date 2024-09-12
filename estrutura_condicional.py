import datetime

# Estrutura condicional
if 10 > 9:
    print("O número 10 é maior que 9")

# Estrutura condicional composta
if 10 > 9:
    print("O número 10 é maior que 9")
elif 10 < 9:
    print("O número 10 é menor que 9")
else:
    print("Os dois são igual")

# Switch 
today = datetime.date.today()
dia_semana = today.weekday()

match dia_semana:
    case 0:
        print("Segunda-feira")
    case 1:
        print("Terça-feira")
    case 2:
        print("Quarta-feira")
    case 3:
        print("Quinta-feira")
    case 4:
        print("Sexta-feira")
    case 4:
        print("Sábado")
    case 6:
        print("Domingo")