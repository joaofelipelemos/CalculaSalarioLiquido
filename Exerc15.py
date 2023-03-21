'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1. salário bruto.
2. quanto pagou ao INSS.
3. quanto pagou ao sindicato.
4. o salário líquido.
5. calcule os descontos e o salário líquido, conforme a tabela abaixo:'''

def calcula_tudo():
    ValorHora = int(input('Quanto recebe por hora? '))
    HorasTrabalhadasDia = int(input('Quantas horas você trabalha por dia? '))
    HorasTrabalhadasMes = HorasTrabalhadasDia * 22

    SalarioBrutoMes = ValorHora * HorasTrabalhadasMes
    DescontoIR = (SalarioBrutoMes * 0.11)
    DescontoINSS = (SalarioBrutoMes * 0.08)
    DescontoSind = (SalarioBrutoMes * 0.05)
    SalarioLiq = SalarioBrutoMes - DescontoINSS-DescontoIR-DescontoSind

    print(f"Seu salário bruto é R$ {SalarioBrutoMes}")
    print(f"Seu desconto do IR é R$ {DescontoIR}")
    print(f"Seu desconto do INSS é R$ {DescontoINSS}")
    print(f"Seu desconto do Sindicato é R$ {DescontoSind}")
    print(f"Seu salário líquido é R$ {SalarioLiq}")

calcula_tudo()
